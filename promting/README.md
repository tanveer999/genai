# Prompt construction
Different techniques for designing a prompt

## Basic prompt
A text input with no context
```
input: twinkle twinkle little star
output: “Twinkle, Twinkle, Little Star” is a classic English nursery rhyme ....
```

## Complex prompt
Basic prompt with context and instruction

The prompt consists:
* input/output pairs containing user input and assistant output
* System message setting the context for assistant behaviour or personality

```
input:
role: system, content: You are a helpful assistant.
role: user, content: Who won the FIFA 2022.
role: assistant, content: Argentina won the FIFA 2022 world cup. 
role: user: Where was it played?

output:
The FIFA World Cup Qatar 2022 was played in Qatar.......
```

## Instruction prompt
Instruction prompt specifies task in more details.

```
Simple:
input: 
Write a description of the Civil War
```

```
Complex:
input: 
Write a description of the Civil War. Provide key dates and events and describe their significance
```

```
Complex with formatting:
input: 
Write a description of the Civil War in 1 paragraph. Provide 3 bullet points with key dates and their significance. Provide 3 more bullet points with key historical figures and their contributions. Return the output as a JSON file
```

## Primary content
This technique has 2 parts:
1. Instruction (Action)
2. Relevant content (That influences the action)

```
Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus.

Summarize this in 2 short sentences
```

Following ways can be used to provide effective instruction
* Examples - Instead of telling model what to do with intruction give it examples and let model infer from the pattern
* Cues - Follow the instruction with a "cue"
* Templates - These are repeatable recipies for prompts with placeholder(variables) that can be customized with data for specific use cases

### Using Examples

Here some example are given with desired output for a given instruction and let model infer the pattern for the desired output.

Based on the number of examples we can have zero shot, one shot , few shot prompting etc.

The prompt has:
1. task description
2. few examples with desired output
3. start of a new example

| Type | Prompt | Output |
|------|--------|--------|
| zero shot | "The sun is rising". Translate to spanish | "El Sol está brillando". |
| one shot | "The sun is rising" => "El Sol está brillando". <br> "Its raining" => | "Está lloviendo." |
| few shot | The player ran the bases => Baseball <br> The player hit an ace => Tennis <br> The player hit a six => Cricket <br> The player made a slam-dunk => | Basketball |

### Prompt cues

In this we nudge the model in direction of desired response format

| Number of cues | Prompt | Output |
|----------------|--------|--------|
| 0 | Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. <br> *Summarize This* | Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass about one-thousandth that of the Sun and more than twice the combined mass of all the other planets. Jupiter is also one of the brightest objects in the night sky and has been known since ancient times. |
| 1 | Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. <br> Summarize This <br> What we learned is that Jupiter | What we learned is that Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a massive gas giant, brighter than most objects in the night sky, and has been known since ancient times. |
| 2 | Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. <br> Summarize This <br> Top 3 Facts We Learned: | Top 3 Facts We Learned: <br> 1. Jupiter is the fifth planet from the Sun and the largest in the Solar System. <br> 2. It is a gas giant with a mass one-thousandth that of the Sun and more than twice the comined mass of all the other planets. <br> 3. It is one of the brightest objects in the night sky and has been known since ancient times. |

### Templates

Predefinie recipies of prompt the can stored and reused to get consistent user experience at scale.

Examples: https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst 


