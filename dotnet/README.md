# Get Started with Semantic Kernel ⚡

## OpenAI / Azure OpenAI API keys

Make sure you have an
[Open AI API Key](https://openai.com/api/) or
[Azure Open AI service key](https://learn.microsoft.com/azure/cognitive-services/openai/quickstart?pivots=rest-api)

## Nuget package

Here is a quick example of how to use Semantic Kernel from a C# console app.
First, let's create a new project, targeting .NET 6 or newer, and add the
`Microsoft.SemanticKernel` nuget package:

    dotnet add package Microsoft.SemanticKernel --prerelease

# Running prompts with input parameters

Copy and paste the following code into your project, with your Azure OpenAI key in hand:

```csharp
using Microsoft.SemanticKernel;

var kernel = Kernel.Builder.Build();

// Azure OpenAI
kernel.Config.AddAzureOpenAITextCompletionService(
    "davinci-azure",                     // Alias used by the kernel
    "text-davinci-003",                  // Azure OpenAI Deployment Name
    "https://contoso.openai.azure.com/", // Azure OpenAI Endpoint
    "...your Azure OpenAI Key..."        // Azure OpenAI Key
);

// Alternative using OpenAI
// kernel.Config.AddOpenAITextCompletionService("davinci-openai",
//     "text-davinci-003",               // OpenAI Model name
//     "...your OpenAI API Key..."       // OpenAI API Key
// );

var prompt = @"{{$input}}

One line TLDR with the fewest words.";

var summarize = kernel.CreateSemanticFunction(prompt);

string text1 = @"
1st Law of Thermodynamics - Energy cannot be created or destroyed.
2nd Law of Thermodynamics - For a spontaneous process, the entropy of the universe increases.
3rd Law of Thermodynamics - A perfect crystal at zero Kelvin has zero entropy.";

string text2 = @"
1. An object at rest remains at rest, and an object in motion remains in motion at constant speed and in a straight line unless acted on by an unbalanced force.
2. The acceleration of an object depends on the mass of the object and the amount of force applied.
3. Whenever one object exerts a force on another object, the second object exerts an equal and opposite on the first.";

Console.WriteLine(await summarize.InvokeAsync(text1));

Console.WriteLine(await summarize.InvokeAsync(text2));

// Output:
//   Energy conserved, entropy increases, zero entropy at 0K.
//   Objects move in response to forces.
```

# Prompt chaining

The previous code shows how to invoke individual semantic functions, but you can
also chain functions (aka prompt chaining) to process the initial input with multiple
operations. 

The following code for example, translates an initial text to math symbols and
then generates a summary:

```csharp
string translationPrompt = @"{{$input}}

Translate the text to math.";

string summarizePrompt = @"{{$input}}

Give me a TLDR with the fewest words.";

var translator = kernel.CreateSemanticFunction(translationPrompt);
var summarize = kernel.CreateSemanticFunction(summarizePrompt);

string inputText = @"
1st Law of Thermodynamics - Energy cannot be created or destroyed.
2nd Law of Thermodynamics - For a spontaneous process, the entropy of the universe increases.
3rd Law of Thermodynamics - A perfect crystal at zero Kelvin has zero entropy.";

// Run two prompts in sequence (prompt chaining)
var output = await kernel.RunAsync(inputText, translator, summarize);

Console.WriteLine(output);

// Output: ΔE = 0, ΔSuniv > 0, S = 0 at 0K.
```

