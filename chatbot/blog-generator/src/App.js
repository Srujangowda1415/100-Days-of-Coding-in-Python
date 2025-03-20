import React, { useState } from "react";
import styled from "styled-components";
import axios from "axios";

const BlogGenerator = () => {
  const [topic, setTopic] = useState("");
  const [wordCount, setWordCount] = useState(500);
  const [tone, setTone] = useState("neutral");
  const [generatedBlog, setGeneratedBlog] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [feedbackGiven, setFeedbackGiven] = useState(false);

  const handleGenerateBlog = async () => {
    if (!topic || !wordCount || !tone) {
      alert("Please fill in all fields");
      return;
    }

    setIsLoading(true);
    setFeedbackGiven(false);

    try {
      const response = await axios.post("http://localhost:5001/generate-blog", {
        topic,
        wordCount,
        tone,
      });

      setGeneratedBlog(formatBlog(response.data.blog));
    } catch (error) {
      console.error("Error generating blog:", error);
      alert("Failed to generate blog");
    } finally {
      setIsLoading(false);
    }
  };

  const formatBlog = (blogText) => {
    const paragraphs = blogText.split("\n").filter(p => p.trim() !== "");
    return paragraphs.map((para, index) => (
      <p key={index}>{para}</p>
    ));
  };

  const handleFeedback = async (isPositive) => {
    try {
      await axios.post("http://localhost:5001/submit-feedback", {
        topic,
        wordCount,
        tone,
        feedback: isPositive ? "positive" : "negative",
      });
      setFeedbackGiven(true);
      alert("Feedback submitted successfully!");
    } catch (error) {
      console.error("Error submitting feedback:", error);
      alert("Failed to submit feedback");
    }
  };

  return (
    <Container>
      <Title>Funky Blog Generator</Title>
      <Form>
        <Input
          type="text"
          placeholder="Enter your blog topic"
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
        />
        <Input
          type="number"
          placeholder="Number of words"
          value={wordCount}
          onChange={(e) => setWordCount(e.target.value)}
        />
        <Select value={tone} onChange={(e) => setTone(e.target.value)}>
          <option value="neutral">Neutral</option>
          <option value="funny">Funny</option>
          <option value="professional">Professional</option>
          <option value="casual">Casual</option>
        </Select>
        <Button onClick={handleGenerateBlog} disabled={isLoading}>
          {isLoading ? "Generating..." : "Generate Blog"}
        </Button>
      </Form>
      {generatedBlog && (
        <BlogContainer>
          <BlogTitle>Your Generated Blog:</BlogTitle>
          <BlogContent>{generatedBlog}</BlogContent>
          {!feedbackGiven && (
            <FeedbackContainer>
              <p>Was this blog helpful?</p>
              <FeedbackButton onClick={() => handleFeedback(true)}>👍 Yes</FeedbackButton>
              <FeedbackButton onClick={() => handleFeedback(false)}>👎 No</FeedbackButton>
            </FeedbackContainer>
          )}
        </BlogContainer>
      )}
    </Container>
  );
};

export default BlogGenerator;

const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
  min-height: 100vh;
  font-family: "Poppins", sans-serif;
`;

const Title = styled.h1`
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 2rem;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
`;

const Form = styled.div`
  display: flex;
  flex-direction: column;
  gap: 1rem;
  background: rgba(255, 255, 255, 0.9);
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
`;

const Input = styled.input`
  padding: 0.75rem;
  border: 2px solid #ddd;
  border-radius: 8px;
  font-size: 1rem;
  outline: none;
  transition: border-color 0.3s ease;

  &:focus {
    border-color: #f6d365;
  }
`;

const Select = styled.select`
  padding: 0.75rem;
  border: 2px solid #ddd;
  border-radius: 8px;
  font-size: 1rem;
  outline: none;
  transition: border-color 0.3s ease;

  &:focus {
    border-color: #f6d365;
  }
`;

const Button = styled.button`
  padding: 0.75rem;
  background: #f6d365;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  color: #333;
  cursor: pointer;
  transition: background 0.3s ease;

  &:hover {
    background: #fda085;
  }

  &:disabled {
    background: #ddd;
    cursor: not-allowed;
  }
`;

const BlogContainer = styled.div`
  margin-top: 2rem;
  background: rgba(255, 255, 255, 0.9);
  padding: 2rem;
  border-radius: 15px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 600px;
`;

const BlogTitle = styled.h2`
  font-size: 1.5rem;
  color: #333;
  margin-bottom: 1rem;
`;

const BlogContent = styled.div`
  font-size: 1rem;
  color: #555;
  line-height: 1.6;
  text-align: left;
`;

const FeedbackContainer = styled.div`
  margin-top: 1rem;
  display: flex;
  gap: 1rem;
  align-items: center;
`;

const FeedbackButton = styled.button`
  background: #f6d365;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.3s ease;
  &:hover {
    background: #fda085;
  }
`;
