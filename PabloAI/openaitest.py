import os
import openai

from config import apikey
openai.api_key = apikey




response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write an email for leave?",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

'''"choices": [
    {
      "text": "\n\nSubject: Request for Leave \n\nDear [Manager\u2019s Name],\n\nI am writing to request a leave of absence from [Date] to [Date].\n\nThe reason for my leave is [Reason]. I have discussed my leave with [name or department] and they are aware that I will be away during this time. I have already [made arrangements/prepared] for my absence, including [arrangements].\n\nI am available to answer any questions and will be available to provide regular updates on my progress. I am also willing to provide support from a remote location should the need arise.\n\nI will need to take [X] days of paid leave, but would be grateful for any unpaid leave days I am able to receive.\n\nI look forward to hearing from you.\n\nSincerely,\n[Your Name]",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 6,
    "completion_tokens": 179,
    "total_tokens": 185
  }
}


'''

print(response)