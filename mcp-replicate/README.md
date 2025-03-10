# Replicate AI Image Generation MCP Server 🖼️

This MCP server allows Claude Desktop to generate images using Replicate's AI models. It provides a simple interface to create images from text prompts using various models like SDXL, Midjourney-style, and more.

## 🚀 Setup

### Prerequisites
- Python 3.10 or higher
- A Replicate account and API token ([Get one here](https://replicate.com/account/api-tokens))
- Claude Desktop

### Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/underdogg4224/welcome-to-cursor.git
   cd welcome-to-cursor/mcp-replicate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API token**
   - Copy `.env.example` to `.env`
   - Add your Replicate API token to the `.env` file
   ```bash
   cp .env.example .env
   # Edit .env with your text editor
   ```

4. **Configure Claude Desktop**
   - Open or create `claude_desktop_config.json` at:
     - Windows: `C:\Users\[YourUsername]\AppData\Roaming\Claude\claude_desktop_config.json`
     - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Add the following configuration:
   ```json
   {
     "mcpServers": {
       "replicate": {
         "command": "python",
         "args": [
           "C:\\path\\to\\welcome-to-cursor\\mcp-replicate\\replicate_server.py"
         ],
         "timeout": 60000
       }
     }
   }
   ```
   - Replace `C:\\path\\to\\` with the actual path to your repository

5. **Restart Claude Desktop**
   - Close and reopen Claude Desktop
   - Look for the hammer 🔨 icon to verify MCP tools are available

## 🎨 Available Models

- **sdxl**: Stability AI's SDXL - High quality, versatile model
- **midjourney**: OpenJourney - Similar style to Midjourney
- **realistic**: Realistic Vision - Photorealistic images
- **pixelart**: Kandinsky - Good for stylized and pixel art
- **anime**: Anything V4 - Anime and illustration style

## 🛠️ Available Tools

### 1. `generate_image`
Generate images from text prompts.

**Parameters:**
- `prompt`: Text description of the image to generate
- `model`: Model to use (sdxl, midjourney, realistic, pixelart, anime)
- `negative_prompt`: Things to avoid in the image
- `width`: Image width (px)
- `height`: Image height (px)
- `num_outputs`: Number of images to generate (1-4)
- `guidance_scale`: How closely to follow the prompt (1-20)
- `num_inference_steps`: Number of diffusion steps (20-50)

### 2. `save_image_to_downloads`
Save an image from a URL to your Downloads folder.

**Parameters:**
- `image_url`: URL of the image to save
- `filename`: Optional filename (without extension)

### 3. `list_available_models`
List all available image generation models.

## 📝 Example Usage in Claude

```
Can you generate an image of a futuristic city with flying cars?

[Claude will use the generate_image tool]

That looks great! Can you save it to my Downloads folder as "future_city"?

[Claude will use the save_image_to_downloads tool]
```

## ⚠️ Troubleshooting

- **API Token Issues**: Make sure your Replicate API token is correctly set in the `.env` file
- **Connection Timeouts**: Increase the timeout value in `claude_desktop_config.json`
- **Model Errors**: Check that you're using a valid model name from the list of available models
- **Image Generation Failures**: Try simplifying your prompt or adjusting parameters

## 📚 Resources

- [Replicate Documentation](https://replicate.com/docs)
- [MCP Protocol Documentation](https://modelcontextprotocol.io/quickstart/server)
- [Claude Desktop Documentation](https://claude.ai/docs)