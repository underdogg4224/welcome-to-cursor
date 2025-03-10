import os
import time
import base64
import tempfile
from typing import List, Optional, Union, Dict, Any
from pathlib import Path
from dotenv import load_dotenv
import replicate
from mcp.server.fastmcp import FastMCP

# Load environment variables from .env file
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("replicate-image-gen")

# Check for API key
REPLICATE_API_TOKEN = os.environ.get("REPLICATE_API_TOKEN")
if not REPLICATE_API_TOKEN:
    print("⚠️ REPLICATE_API_TOKEN not found in environment variables or .env file")
    print("Please set your Replicate API token before using this server")
    print("You can get one at: https://replicate.com/account/api-tokens")

# Available models
MODELS = {
    "sdxl": "stability-ai/sdxl:c221b2b8ef527988fb59bf24a8b97c4561f1c671f73bd389f866bfb27c061316",
    "midjourney": "prompthero/openjourney:9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb",
    "realistic": "lucataco/realistic-vision-v5:154b7e4a34b891e3e8bb19cefca242b2c89f2b0ce3c075ebb28f5d4b4538b2f0",
    "pixelart": "ai-forever/kandinsky-2:601eea49d49003e4d6fc0edcb1638ee4e4e5a1ac2e5e244ecf1da9476d9c0695",
    "anime": "cjwbw/anything-v4.0:42a996d39a96aedc57b2e0aa8105dea39c9c89d9d266caf6bb4327a1c172fea4"
}

# Default parameters
DEFAULT_PARAMS = {
    "width": 768,
    "height": 768,
    "num_outputs": 1,
    "guidance_scale": 7.5,
    "num_inference_steps": 30
}

@mcp.tool()
def generate_image(
    prompt: str,
    model: str = "sdxl",
    negative_prompt: str = "",
    width: int = 768,
    height: int = 768,
    num_outputs: int = 1,
    guidance_scale: float = 7.5,
    num_inference_steps: int = 30
) -> List[str]:
    """Generate images using Replicate AI models.
    
    Args:
        prompt: Text description of the image to generate
        model: Model to use (sdxl, midjourney, realistic, pixelart, anime)
        negative_prompt: Things to avoid in the image
        width: Image width (px)
        height: Image height (px)
        num_outputs: Number of images to generate (1-4)
        guidance_scale: How closely to follow the prompt (1-20)
        num_inference_steps: Number of diffusion steps (20-50)
    
    Returns:
        List of image URLs
    """
    if not REPLICATE_API_TOKEN:
        return ["Error: REPLICATE_API_TOKEN not set. Please set your API token."]
    
    # Validate model
    if model not in MODELS:
        return [f"Error: Model '{model}' not found. Available models: {', '.join(MODELS.keys())}"]
    
    # Validate parameters
    if num_outputs < 1 or num_outputs > 4:
        num_outputs = min(max(1, num_outputs), 4)
    
    if guidance_scale < 1 or guidance_scale > 20:
        guidance_scale = min(max(1, guidance_scale), 20)
    
    if num_inference_steps < 20 or num_inference_steps > 50:
        num_inference_steps = min(max(20, num_inference_steps), 50)
    
    # Prepare parameters
    params = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "width": width,
        "height": height,
        "num_outputs": num_outputs,
        "guidance_scale": guidance_scale,
        "num_inference_steps": num_inference_steps
    }
    
    # Different models have different parameter names
    if model == "sdxl":
        # SDXL specific parameters
        params["refine"] = "expert_ensemble_refiner"
        params["scheduler"] = "K_EULER"
    elif model == "midjourney":
        # OpenJourney specific parameters
        params["scheduler"] = "DPMSolverMultistep"
        params["prompt"] = f"mdjrny-v4 style {prompt}"
    
    try:
        # Run the model
        output = replicate.run(
            MODELS[model],
            input=params
        )
        
        # Return the image URLs
        return output
    except Exception as e:
        return [f"Error generating image: {str(e)}"]

@mcp.tool()
def save_image_to_downloads(image_url: str, filename: Optional[str] = None) -> str:
    """Save an image from URL to Downloads folder.
    
    Args:
        image_url: URL of the image to save
        filename: Optional filename (without extension)
    
    Returns:
        Path to the saved file
    """
    import httpx
    
    # Get Downloads folder
    downloads_folder = str(Path.home() / "Downloads")
    
    # Generate filename if not provided
    if not filename:
        timestamp = int(time.time())
        filename = f"replicate-image-{timestamp}"
    
    # Ensure filename has .png extension
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        filename += ".png"
    
    # Full path
    filepath = os.path.join(downloads_folder, filename)
    
    try:
        # Download the image
        with httpx.stream("GET", image_url) as response:
            response.raise_for_status()
            with open(filepath, "wb") as f:
                for chunk in response.iter_bytes():
                    f.write(chunk)
        
        return f"Image saved to: {filepath}"
    except Exception as e:
        return f"Error saving image: {str(e)}"

@mcp.tool()
def list_available_models() -> Dict[str, str]:
    """List all available image generation models.
    
    Returns:
        Dictionary of model names and descriptions
    """
    return {
        "sdxl": "Stability AI's SDXL - High quality, versatile model",
        "midjourney": "OpenJourney - Similar style to Midjourney",
        "realistic": "Realistic Vision - Photorealistic images",
        "pixelart": "Kandinsky - Good for stylized and pixel art",
        "anime": "Anything V4 - Anime and illustration style"
    }

if __name__ == "__main__":
    # Run the server
    print("🚀 Starting Replicate Image Generation MCP Server")
    print(f"📋 Available models: {', '.join(MODELS.keys())}")
    if REPLICATE_API_TOKEN:
        print("✅ API token found")
    else:
        print("⚠️ API token not found - please set REPLICATE_API_TOKEN")
    
    mcp.run()