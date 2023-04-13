# Semantic Kernel

[![Python package](https://img.shields.io/pypi/v/semantic-kernel)](https://pypi.org/project/semantic-kernel/)
[![Nuget package](https://img.shields.io/nuget/vpre/Microsoft.SemanticKernel)](https://www.nuget.org/packages/Microsoft.SemanticKernel/)
[![dotnet](https://github.com/microsoft/semantic-kernel/actions/workflows/dotnet-ci.yml/badge.svg?branch=main)](https://github.com/microsoft/semantic-kernel/actions/workflows/dotnet-ci.yml)
[![License: MIT](https://img.shields.io/github/license/microsoft/semantic-kernel)](https://github.com/microsoft/semantic-kernel/blob/main/LICENSE)
[![Discord](https://img.shields.io/discord/1063152441819942922)](https://aka.ms/SKDiscord)

> ℹ️ **NOTE**: This project is in early alpha and, just like AI, will evolve quickly.
> We invite you to join us in developing the Semantic Kernel together!
> Please contribute by
> using GitHub [Discussions](https://github.com/microsoft/semantic-kernel/discussions),
> opening GitHub [Issues](https://github.com/microsoft/semantic-kernel/issues/new/choose),
> sending us [PRs](https://github.com/microsoft/semantic-kernel/pulls),
> joining our [Discord community](https://aka.ms/SKDiscord).

**Semantic Kernel (SK)** is a lightweight SDK enabling integration of AI Large
Language Models (LLMs) with conventional programming languages. The SK extensible
programming model combines natural language **semantic functions**, traditional
code **native functions**, and **embeddings-based memory** unlocking new potential
and adding value to applications with AI.

SK supports
[prompt templating](docs/PROMPT_TEMPLATE_LANGUAGE.md), function
chaining,
[vectorized memory](docs/EMBEDDINGS.md), and
[intelligent planning](docs/PLANNER.md)
capabilities out of the box.

![image](https://user-images.githubusercontent.com/371009/221739773-cf43522f-c1e4-42f2-b73d-5ba84e21febb.png)

Semantic Kernel is designed to support and encapsulate several design patterns from the
latest in AI research, such that developers can infuse their applications with complex
[skills](docs/SKILLS.md) like [prompt](docs/PROMPT_TEMPLATE_LANGUAGE.md) chaining,
recursive reasoning, summarization, zero/few-shot learning, contextual memory,
long-term memory, [embeddings](docs/EMBEDDINGS.md), semantic indexing, [planning](docs/PLANNER.md),
and accessing external knowledge stores as well as your own data.

By joining the SK community, you can build AI-first apps faster and have a front-row
peek at how the SDK is being built. SK has been released as open-source so that more
pioneering developers can join us in crafting the future of this landmark moment
in the history of computing.

## Get Started with Semantic Kernel ⚡

Semantic Kernel is available to explore AI and build apps with C# and Python:

<div style="display:flex;height:30px;padding:5px 0 5px 10px;">
<img src="https://user-images.githubusercontent.com/371009/230673036-fad1e8e6-5d48-49b1-a9c1-6f9834e0d165.png" style="margin-right:12px" height="30"/>
<a href="dotnet/README.md">Using Semantic Kernel in C#</a>.
</div>

<div style="display:flex;height:30px;padding:5px 0 5px 10px;">
<img src="https://user-images.githubusercontent.com/371009/230673733-7a447d30-b48e-46e1-bd84-2b321c90649e.png" style="margin-right:12px" height="30"/>
<a href="python/README.md">Using Semantic Kernel in Python</a>.
</div>

## Samples ⚡

If you would like a quick overview about how Semantic Kernel can integrate with your
app, start by cloning the repository:

```shell
git clone https://github.com/microsoft/semantic-kernel.git
```

and try these examples:

|                                                                         |                                                                                                                                   |
| ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| [Simple chat summary](samples/apps/chat-summary-webapp-react/README.md) | Use ready-to-use skills and get those skills into your app easily.                                                                |
| [Book creator](samples/apps/book-creator-webapp-react/README.md)        | Use planner to deconstruct a complex goal and envision using the planner in your app.                                             |
| [Authentication and APIs](samples/apps/auth-api-webapp-react/README.md) | Use a basic connector pattern to authenticate and connect to an API and imagine integrating external data into your app's LLM AI. |
| [GitHub repository Q&A](samples/apps/github-qna-webapp-react/README.md) | Use embeddings and memory to store recent data and allow you to query against it.                                                 |
| [Copilot Chat Sample App](samples/apps/copilot-chat-app/README.md)      | Build your own chat experience based on Semantic Kernel.                                                                          |

For a more hands-on overview, you can also run the
[Getting Started with C# notebook](samples/notebooks/dotnet/Getting-Started-Notebook.ipynb) and
[Getting Started with Python notebook](samples/notebooks/python/Getting-Started-Notebook.ipynb),
looking into the syntax, creating
[Semantic Functions](docs/GLOSSARY.md),
working with Memory, and see how the kernel works.

**Please note:**

- You will need an
  [Open AI API Key](https://openai.com/api/) or
  [Azure Open AI service key](https://learn.microsoft.com/azure/cognitive-services/openai/quickstart?pivots=rest-api)
  to get started.
- There are a few software requirements you may need to satisfy before running examples and notebooks:
  1. [Azure Functions Core Tools](https://learn.microsoft.com/azure/azure-functions/functions-run-local)
     used for running the kernel as a local API, required by the web apps.
  2. [Yarn](https://yarnpkg.com/getting-started/install) used for installing
     web apps' dependencies.
  3. Semantic Kernel supports .NET Standard 2.1 and it's recommended using .NET 6+. However, some of
     the examples in the repository require [.NET 7](https://dotnet.microsoft.com/download) and the VS Code
     [Polyglot extension](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.dotnet-interactive-vscode)
     to run the notebooks.

## Contributing and Community

We welcome your contributions and suggestions to SK community! One of the easiest
ways to participate is to engage in discussions in the GitHub repository.
Bug reports and fixes are welcome!

For new features, components, or extensions, please open an issue and discuss with
us before sending a PR. This is to avoid rejection as we might be taking the core
in a different direction, but also to consider the impact on the larger ecosystem.

To learn more and get started:

- Read the [documentation](https://aka.ms/sk/learn)
- Learn how to [contribute](https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md) to the project
- Join the [Discord community](https://aka.ms/SKDiscord)
- Follow the team on our [blog](https://aka.ms/sk/blog)

## Code of Conduct

This project has adopted the
[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the
[Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
or contact [opencode@microsoft.com](mailto:opencode@microsoft.com)
with any additional questions or comments.

## License

Copyright (c) Microsoft Corporation. All rights reserved.

Licensed under the [MIT](LICENSE) license.
