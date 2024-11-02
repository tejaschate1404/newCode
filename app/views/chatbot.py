from django.views import View
from django.http import JsonResponse
from django.shortcuts import render

class ChatBotView(View):
    template_name = 'app/chatbot.html'

    def get(self, request, *args, **kwargs):
        # Render the chatbot template
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        # Get user input from POST request
        user_message = request.POST.get('message')
        
        # Process the message and generate a response (simple example)
        if "hello" in user_message.lower():
            bot_response = "Hi there! How can I help you?"
        elif "bye" in user_message.lower():
            bot_response = "Goodbye! Have a great day!"
        else:
            bot_response = "I'm sorry, I didn't understand that."

        # Return the response as JSON for dynamic updates
        return JsonResponse({'response': bot_response})
