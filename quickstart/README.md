# Cursor IDE Quickstart Guide 🚀

This quickstart guide will help you get up and running with Cursor IDE in minutes!

## 1. Installation 📥

1. **Download Cursor**
   - Visit [cursor.so](https://cursor.so)
   - Click "Download for Windows"
   - Run the installer

2. **First Launch**
   - Open Cursor
   - Sign in (optional but recommended for AI features)
   - Choose your preferred theme

## 2. Essential Commands 🎯

### AI Chat Commands (Ctrl + L)
```
/explain - Explain selected code
/fix - Fix issues in selected code
/test - Generate tests for selected code
/docs - Generate documentation
```

### Basic Shortcuts
```
Ctrl + L         : Open AI Chat
Ctrl + P         : Quick File Open
Ctrl + Shift + P : Command Palette
Ctrl + B         : Toggle Sidebar
Ctrl + ,         : Open Settings
```

## 3. Quick Examples 💡

### Generate Code with AI
1. Press `Ctrl + L`
2. Type something like:
   ```
   Create a function that calculates fibonacci numbers
   ```

### Get Code Explanations
1. Select code
2. Press `Ctrl + L`
3. Type `/explain`

### Fix Code Issues
1. Select problematic code
2. Press `Ctrl + L`
3. Type `/fix`

## 4. MCP Setup (Message Channel Protocol) 🔌

### Basic Configuration
```json
{
    "mcpServers": {
        "filesystem": {
            "command": "C:\\Windows\\System32\\cmd.exe",
            "args": [
                "/c",
                "npx",
                "-y",
                "@modelcontextprotocol/server-filesystem",
                "C:\\Users\\[YourUsername]\\Desktop",
                "C:\\Users\\[YourUsername]\\Downloads"
            ],
            "timeout": 30000
        }
    }
}
```

Save this to: `C:\Users\[YourUsername]\AppData\Roaming\Claude\claude_desktop_config.json`

### Requirements
- Node.js installed
- Python (optional, for Python development)
- Git (for version control)

## 5. Common Tasks 📝

### Starting a New Project
1. File → New Window
2. Select folder location
3. Start coding or use AI to scaffold project

### Using Version Control
1. View → Source Control
2. Initialize repository
3. Make commits through UI

### Using AI Effectively
1. Be specific in requests
2. Provide context when needed
3. Use code blocks for examples
4. Review and modify AI suggestions

## 6. Troubleshooting 🔧

### AI Not Responding
1. Check internet connection
2. Verify sign-in status
3. Restart Cursor

### MCP Issues
1. Verify Node.js installation
2. Check configuration paths
3. Run servers manually to test
4. Check for timeouts

### Performance Issues
1. Close unused windows
2. Clear cache if needed
3. Update to latest version

## 7. Next Steps 🎯

1. Try the AI chat features
2. Customize your settings
3. Join the [Discord community](https://discord.gg/cursor)
4. Explore advanced features

## Need Help? 🆘

- Check [Documentation](https://cursor.so/docs)
- Join Discord community
- Report issues on GitHub
- Use AI chat for coding help