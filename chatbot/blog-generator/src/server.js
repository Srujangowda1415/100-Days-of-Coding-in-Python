const express = require("express");
const cors = require("cors");
const axios = require("axios");

const app = express();
const PORT = 5001;

app.use(cors());
app.use(express.json());

// Configuration for model selection
const config = {
  provider: "groq",
  model: "mixtral-8x7b-32768",
  groq_api_url: "https://api.groq.com/openai/v1/chat/completions",
  groq_api_key: "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", // Replace with actual API key
};

// In-memory JSON variables to store feedback
let positive_feedback = [];
let negative_feedback = [];

// Function to generate a blog using Groq
const generateBlog = async (topic, wordCount, tone) => {
  try {
    const prompt = `
      Generate a structured blog post about **"${topic}"** in **${wordCount} words**, using a **${tone} tone**.

      **Formatting Guidelines:**
      - Start with a **bold title**.
      - Write an engaging introduction (2-3 sentences).
      - Use **clear sections with subheadings**.
      - End with a **conclusion**.
    `;

    const response = await axios.post(
      config.groq_api_url,
      {
        model: config.model,
        messages: [{ role: "user", content: prompt }],
        max_tokens: 1024,
      },
      {
        headers: {
          Authorization: `Bearer ${config.groq_api_key}`,
          "Content-Type": "application/json",
        },
      }
    );

    return response.data.choices[0].message.content;
  } catch (error) {
    console.error("Error generating blog:", error.response?.data || error.message);
    return "Failed to generate blog.";
  }
};

// API to generate a blog
app.post("/generate-blog", async (req, res) => {
  const { topic, wordCount, tone } = req.body;
  if (!topic || !wordCount || !tone) {
    return res.status(400).json({ error: "Missing required fields." });
  }

  const blog = await generateBlog(topic, wordCount, tone);
  res.json({ blog });
});

// API to store feedback in variables
app.post("/submit-feedback", (req, res) => {
  const { blog, feedback } = req.body;

  if (!blog || !feedback) {
    return res.status(400).json({ error: "Missing blog content or feedback type." });
  }

  if (feedback === "positive") {
    positive_feedback.push(blog);
  } else if (feedback === "negative") {
    negative_feedback.push(blog);
  } else {
    return res.status(400).json({ error: "Invalid feedback type." });
  }

  res.json({ message: "Feedback submitted successfully!" });
});

// API to retrieve stored feedback
app.get("/get-feedback", (req, res) => {
  res.json({ positive_feedback, negative_feedback });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
