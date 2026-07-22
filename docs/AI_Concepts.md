# AI Concepts

## Table of Contents

1. [Artificial Intelligence](#1-artificial-intelligence)
2. [Machine Learning (ML)](#2-machine-learning-ml)
3. [Neural Networks (NN)](#3-neural-networks-nn)
4. [Deep Learning (DL)](#4-deep-learning-dl)
5. [NLP (Natural Language Processing)](#5-nlp-natural-language-processing)
6. [Large Language Models (LLMs)](#6-large-language-models-llms)
7. [LLM Types](#7-llm-types)
8. [LLM Model Types](#8-llm-model-types)
9. [Generative AI](#9-generative-ai)

Each section builds on the last: AI is the broad umbrella; ML is how machines learn within it; Neural Networks and Deep Learning are a particular way of doing ML; NLP applies all of that to language; and LLMs are today's dominant NLP architecture, powering the Generative AI systems covered at the end.

## 1. Artificial Intelligence

A big umbrella. AI refers to machines that **mimic human intelligence**, performing tasks like ***learning, reasoning, problem-solving, and decision-making***.

Types of AI:

- **Narrow/Weak AI &mdash;** AI specialized in one task. (e.g. Google Search, Siri)
- **General/Strong AI &mdash;** Hypothetical AI that can perform multiple tasks or AI with human-like intelligence. (e.g. ChatGPT, Google Bard)
- **Super AI &mdash;** AI that surpasses human intelligence. (not yet achieved)

## 2. Machine Learning (ML)

A subset of AI that enables machines to learn from data without explicit programming. It identifies patterns and makes predictions.

**Types of ML**:

- **Supervised Learning &mdash;** Uses **labelled data** to learn patterns. (e.g. housing prices).
- **Unsupervised Learning &mdash;** Finds hidden patterns in **unlabelled data**. (e.g. customer segmentation)
- **Reinforcement Learning &mdash;** Learns from rewards and penalties. (e.g. playing video games)

## 3. Neural Networks (NN)

The brain of AI models. A neural network is a machine learning model inspired by how the human brain works — a series of algorithms, made of interconnected units called neurons, that learn patterns from data and map inputs to outputs.

**Neural Networks are the backbone/foundation for Deep Learning architectures like CNNs, RNNs, and Transformers**, and power many modern AI systems, including vision, speech, and language models.

Components of a Neural Network:

- **Input Layer &mdash;** receives the input data and passes it to the hidden layers.
- **Hidden Layers &mdash;** process the input data and extract features from it.
- **Output Layer &mdash;** generates the output based on the input data and the hidden layers.
- **Weights & Biases &mdash;** the parameters that determine how strongly signals influence predictions.
- **Activation Functions &mdash;** introduce non-linearity so the model can learn complex patterns.
- **Loss Function &mdash;** measures the difference between the predicted output and the actual output.
- **Backpropagation &mdash;** adjusts the weights of the neural network to minimize the loss function.
- **Training &mdash;** uses forward propagation + backpropagation to reduce error over time.
- **Testing &mdash;** uses the trained neural network to predict the output for new, unseen input data.

## 4. Deep Learning (DL)

A more advanced form of ML. **Deep Learning is a subset of ML that uses multiple layers of neural networks** (deep neural networks) to process **complex** data.

ML works well with structured data, while DL handles large, unstructured datasets (e.g. images, text, speech).

## 5. NLP (Natural Language Processing)

NLP is a branch of AI that enables computers to understand, interpret, and generate human language.

NLP Tasks:

- **Tokenization &mdash;** Breaking down a sentence into individual words or sentences.
- **Sentiment Analysis &mdash;** Detecting the sentiment or emotions in a text.
- **Named Entity Recognition (NER) &mdash;** Identifying and categorizing named entities (people/places/organizations) in a text.

**Modern NLP models are powered by Deep Learning and LLMs.**

## 6. Large Language Models (LLMs)

The brains behind modern AI. LLMs are massive deep learning models — built from the neural network and Transformer concepts above — trained on vast amounts of text data to perform NLP tasks.

**LLMs are the foundation of Generative AI and Conversational AI.**

## 7. LLM Types

**Frontier or Foundational or Closed-Source Models &mdash;** Models that are made by a company and are closed-source. (e.g. OpenAI GPT, Anthropic Claude, Google Gemini, X Grok, Mistral etc.)

**Open Source or Open Weight Models &mdash;** Models that are made by a company/community and are open-source. (e.g. OpenAI GPT-OSS, Meta Llama, DeepSeek, Google Gemma, Microsoft Phi, Alibaba Qwen, etc.)

Mistral - A type of model called a mixture of experts, which means that it has lots of smaller models within it, and it directs traffic to different specialist models depending on the kind of question you're asking.

DeepSeek - Developed with a fraction of the cost ($4M) that OpenAI spent for GPT ($100M).

They're not actually DeepSeek — those are smaller variations of DeepSeek. They are in fact versions of Llama and Qwen. Small versions of Llama and Qwen were trained further with synthetic data generated by the big DeepSeek model: big DeepSeek generated lots of fake/synthetic training data, and that data was used to educate these smaller Llama and Qwen models. This process is known as **Distillation**. There are various ways to perform distillation; the above approach is one of them.

**Cloud Managed &mdash;** Services that are made and hosted in the cloud and inherently use different models. (e.g. OpenAI ChatGPT, Claude, Google Vertex, Microsoft Phi, AWS Bedrock, X Groq, OpenRouter etc.)

## 8. LLM Model Types

**Base Models &mdash;** Take a sequence of information as input and predict what comes next. Better for when you're training a model for fine-tuning to learn a new skill.

**Chat or Instruct Variant Models &mdash;** Take a question and give an answer, following prompt style. They use Reinforcement Learning from Human Feedback (RLHF) and follow a Chain-of-Thought (CoT) approach. They are faster and cheaper, and better suited for interactive use cases and creative content generation.

**Reasoning/Thinking Models &mdash;** Also trained with RLHF and a Chain-of-Thought (CoT) approach, but trained to first output their thinking steps and then give an answer. The amount of reasoning it does is called **Reasoning Budget or Reasoning Effort**. This technique is called **Budget Forcing**. **They are better for problem solving**.

**Hybrid Models &mdash;** A variation combining thinking models and chat models.

## 9. Generative AI

Generative AI refers to AI models that generate new content — text, images, music, or videos — based on training data.

Key Technologies:

- **GANs (Generative Adversarial Networks) &mdash;** A type of neural network used to generate new data. Used in deepfake creation.
- **Transformer Models &mdash;** Powering LLMs like ChatGPT, Gemini, and Claude.

[AI Map](ai_map.html)
