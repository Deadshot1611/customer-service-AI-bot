# AI Customer Service Bot

This project is an AI Customer Service Bot built using the Kaludi/Customer-Support-Assistant-V2 model from Hugging Face and the Transformers library. The bot can efficiently handle customer inquiries and support requests, improving customer service operations.

## Features

- Understands and responds to customer queries
- Provides accurate and helpful information
- Streamlines customer support processes
- Accessible via a user-friendly web interface

## Technologies Used

- **Model:** Kaludi/Customer-Support-Assistant-V2
- **Framework:** Transformers
- **API Integration:** FastAPI
- **User Interface:** Gradio
- **Deployment:** Hugging Face Spaces

## Setup and Installation

1. **Clone the repository:**

    \`\`\`bash
    git clone https://github.com/Deadshot1611/customer-service-AI-bot.git
    cd customer-service-bot
    \`\`\`

2. **Install the required packages:**

    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

3. **Run the FastAPI server:**

    \`\`\`bash
    uvicorn main:app --reload
    \`\`\`

4. **Access the Gradio interface:**

    The Gradio interface will be available at `https://deadshot2003-customerservice-bot.hf.space/`.

## Usage

- Open the Gradio interface in your web browser.
- Type your customer query in the input box and hit enter.
- The chatbot will provide helpful and accurate responses.

## Deployment

The bot is deployed on Hugging Face Spaces. You can access it [here](https://deadshot2003-customerservice-bot.hf.space/).

## Contributing

Feel free to open issues or submit pull requests if you would like to contribute to the project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
