# Copyright (c) Microsoft. All rights reserved.

import asyncio

from utils import e2e_text_completion

import semantic_kernel as sk
import semantic_kernel.connectors.ai.hugging_face as sk_hf

kernel = sk.Kernel()

# Configure LLM service
kernel.config.add_text_completion_service(
    "gpt2", sk_hf.HuggingFaceTextCompletion("gpt2", task="text-generation")
)

asyncio.run(e2e_text_completion.simple_completion(kernel))
