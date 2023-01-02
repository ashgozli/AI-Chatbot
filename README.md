# Ecommerce AI-Chatbot in PyTorch 🤖
![AI-Chatbot Output Example](https://user-images.githubusercontent.com/88709547/210194061-380c0b43-afeb-4497-93ef-40ec0aed2547.png)
 
## **Anaconda Installation & Environment Setup**

### Manual installation of PyTorch in a conda environment:
1. Create a conda environment with conda:
### `create -n my-torch python=3.7 -y`
2. Activate the new environment with:
### `conda activate my-torch`
3. Inside the new environment, install PyTorch and related packages with:
### `conda install python=3.6 pytorch torchvision matplotlib pandas -c pytorch`
### ⚠️ Note: If you you don’t specify a version, conda will install the latest PyTorch.

4. Install PyTorch dependency used in this project:
### `pip install nltk`
### ⚠️ Note: You need to be installing the nltk package in your created PyTorch environment 

## **Usage** 

### Run the commands in order: 
### `python train.py`
- This command trains the data using a [Feed Forward Neural Net](https://deepai.org/machine-learning-glossary-and-terms/feed-forward-neural-network) with 2 hidden layers. 
- Creates a `data.pth` for `chat.py` to utilize. 
### `python chat.py`

## **Intents Customization**
The Chatbot is not limited to only ecommerce purposes. You can create your own custom tags, patterns, and responses in the Ecommerce_Intents.json file to use the Chatbot for any purpose. This allows you to input your own data and customize the Chatbot to fit your needs.

- To create your own `tags`, `patterns`, and `responses`, you will need to open the `Ecommerce_Intents.json` file. This file contains a list of intents, which are a combination of a tag, pattern, and response.

- To create a new intent, you will need to add a new object to the list of intents. Each intent object should contain the following properties:

  - **`tag`**: This is a string that represents the category or topic of the intent. You can use existing tags or create your own.

  - **`patterns`**: This is a list of strings that represent the different ways that a user might ask about the topic associated with the intent. You can use existing patterns or create your own.

  - **`responses`**: This is a list of strings that represent the possible responses that the Chatbot can give when it recognizes an intent. You can use existing responses or create your own.
    
```
{
  "intents": [
    {
      "tag": "view_order_status",
      "patterns": [
        "What is the status of my order?",
        "Can you tell me the status of my order?",
        "I'd like to know the status of my order",
        "I'm curious about the status of my order"
      ],
      "responses": [
        "Sure! I can check the status of your order. Can you please provide your order number?",
        "No problem! In order to check the status of your order, I'll need your order number. Do you have it handy?",
        "Of course! In order to look up the status of your order, I'll need your order number. Can you provide that for me?",
        "Absolutely! I can help you with that. In order to check the status of your order, I'll need your order number. Do you have that available?"
      ]
    },
    {
      "tag": "cancel_order",
      "patterns": [
        "I'd like to cancel my order",
        "Can you cancel my order?",
        "I want to cancel my order",
        "I need to cancel my order"
      ],
      "responses": [
        "Sure thing! I can cancel your order for you. Can you please provide your order number?",
        "No problem! In order to cancel your order, I'll need your order number. Do you have it handy?",
        "Of course! In order to cancel your order, I'll need your order number. Can you provide that for me?",
        "Absolutely! I can help you with that. In order to cancel your order, I'll need your order number. Do you have that available?"
      ]
    },
    ...
  ]
}
```

Once you have added your custom tags, patterns, and responses to the Ecommerce_Intents.json file, you can use them in the Chatbot by including them in the appropriate place in your code.

By following these steps, you can customize the Chatbot to fit your specific needs and use it for any purpose beyond just ecommerce.

## Credits

- The design of the Chatbot was inspired and guided by [Patrick Loeber](https://github.com/patrickloeber) under the MIT license.
- Additional usage of articles such as: [Chatbot Magazine](https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077) and [Deep AI](https://deepai.org/machine-learning-glossary-and-terms/feed-forward-neural-network)





