# Voice Impairement 

### Overview
Modern voice-driven technologies rely heavily on Automatic Speech Recognition (ASR). However, most ASR systems are trained primarily on fluent speech, making them ineffective for users with speech impairments such as stuttering. This project aims to design an inclusive AI system capable of understanding and correcting disfluent speech, ensuring equitable access to digital communication.

### The Accessibility Challenge

Voice assistants, dictation tools, and transcription systems are now essential to daily digital interaction. Yet, they often fail to correctly interpret stuttered speech, leading to:

- Misrecognition of words
- User frustration
- Limited access to essential digital services
- A widening accessibility gap for millions of affected individuals

### Problem Statement
In today’s voice-driven world, technologies such as voice assistants, speech-to-text systems, and transcription tools often fail to understand users with speech impairments like stuttering. This creates a major
accessibility gap, preventing individuals from fully benefiting from digital communication tools. The problem lies in the inability of existing ASR (Automatic Speech Recognition) models to handle disfluent speech patterns.

### Key statistics include:

- Large global population experiencing stuttering

- Increased error rates for disfluent speech

- Persistent prevalence among adults

- Project Vision: Inclusive AI

This project aims to build an AI system capable of recognizing and correcting stuttered speech. By teaching models to understand disfluent patterns, we move towards accessible communication tools that support independence and inclusivity.

 ### System Architecture
1. Input Acquisition: Users provide voice input via recording or file upload.

2. Audio Preprocessing:
   Normalization: Standardizes audio levels
   Noise Reduction: Filters background noise
   Pause Detection: Identifies silences and breaks in speech

3. Feature Extraction
   Spectrograms: Visual frequency representations
   MFCCs: Core acoustic features extracted for model analysis

5. ASR and Text Correction

   Whisper ASR: Fine-tuned to recognize disfluent patterns
   Transformer-based Correction: Converts raw disfluent text into clean, fluent text by understanding context and removing repetitions

5. Output Generation

Produces refined text or optionally converts it into synthesized fluent speech through TTS.

Preprocessing Pipeline

Normalization – ensures consistent volume

Noise Reduction – isolates speech from ambient interference

Pause Detection – marks silence regions for contextual understanding

Feature Extraction and Recognition

Spectrograms and MFCCs capture essential acoustic information

Whisper ASR serves as the primary speech recognition engine, fine-tuned for disfluency robustness

Text Correction Intelligence

A Transformer sequence-to-sequence model analyzes the ASR output, removes disfluent patterns, identifies intended text, and reconstructs grammatically and semantically correct sentences.

Impact and Future Scope
Digital Inclusion

Enables accessible and fair usage of voice-enabled systems.

Educational Access

Supports students with speech impairments using voice-assisted learning.

Professional Empowerment

Facilitates participation in meetings, presentations, and communication workflows.

Universal Design

Contributes to the broader movement toward inclusive AI systems that accommodate diverse speech patterns.
