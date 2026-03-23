# 📚 EduMate - Your AI Study Buddy

A modern React-based chatbot application designed to help university students with their studies, particularly computer science concepts.

## ✨ Features

- **🎨 Modern UI**: Beautiful gradient design with smooth animations
- **💬 Persistent Chat**: Maintains conversation history for context
- **🧠 AI-Powered**: Uses OpenRouter API with GPT-4o-mini model
- **📚 Study-Focused**: Specializes in academic and CS topics
- **🚀 Fast & Responsive**: Built with React and Vite
- **🔒 Secure**: Environment variable management for API keys

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd edumate
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Set Up Environment Variables
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your OpenRouter API key
VITE_OPENROUTER_API_KEY=sk-or-v1-your-api-key-here
```

Get your API key from: [OpenRouter API Keys](https://openrouter.ai/keys)

### 4. Run the Development Server
```bash
npm run dev
```

### 5. Build for Production
```bash
npm run build
```

## 🌐 Deployment

### GitHub Pages
1. Build the project: `npm run build`
2. Deploy the `dist` folder to GitHub Pages
3. Set up your environment variables in your deployment platform

### Vercel/Netlify
1. Connect your GitHub repository
2. Set build command: `npm run build`
3. Set output directory: `dist`
4. Add environment variable: `VITE_OPENROUTER_API_KEY`

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `VITE_OPENROUTER_API_KEY` | Your OpenRouter API key | Yes |

### Supported Models

Currently configured to use `openai/gpt-4o-mini`. You can modify the model in `src/App.tsx`:

```typescript
body: JSON.stringify({
  model: 'openai/gpt-4o-mini', // Change this to your preferred model
  // ... other parameters
})
```

## 📖 Usage Examples

### Great Questions to Ask EduMate:

- "Explain binary search in simple terms"
- "What's the difference between arrays and linked lists?"
- "How does recursion work? Give me an example"
- "What is Big O notation and why is it important?"
- "Explain object-oriented programming concepts"
- "How do I approach dynamic programming problems?"

## 🛠️ Technical Details

### Tech Stack:
- **Frontend**: React 18 + TypeScript
- **Build Tool**: Vite
- **Styling**: Tailwind CSS
- **Icons**: Lucide React
- **AI**: OpenRouter API (GPT-4o-mini)

### Project Structure:
```
edumate/
├── src/
│   ├── App.tsx           # Main React component
│   ├── main.tsx          # React entry point
│   ├── index.css         # Tailwind imports
│   └── vite-env.d.ts     # Vite type definitions
├── public/               # Static assets
├── .env.example          # Environment variables template
├── .env                  # Your environment variables (create this)
├── package.json          # Dependencies and scripts
├── tailwind.config.js    # Tailwind configuration
├── vite.config.ts        # Vite configuration
└── README.md            # This file
```

## 🔒 Security

- API keys are managed through environment variables
- No sensitive data is committed to the repository
- HTTPS is used for all API communications
- Input validation prevents malicious requests

## 🐛 Troubleshooting

### Common Issues:

1. **"API key not found" error**
   - Make sure `.env` file exists in the project root
   - Check that `VITE_OPENROUTER_API_KEY` is correctly set
   - Restart the dev server after adding the key

2. **"API request failed" error**
   - Check your internet connection
   - Verify your OpenRouter API key is valid
   - Check if you have sufficient credits on OpenRouter

3. **Build fails**
   - Make sure all dependencies are installed: `npm install`
   - Check that environment variables are set correctly
   - Try deleting `node_modules` and running `npm install` again

## 📱 Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

---

**Happy Studying! 📚✨**

Built with ❤️ for students, by students.