from dotenv import load_dotenv
import os
from google import genai

class GeminiAPI():
    """
    A class to interact with the Gemini API for generating content.

    Attributes:
    -----------
    key : str
        The API key for authenticating with the Gemini service.
    model : genai.GenerativeModel
        The generative model used for content generation.

    Methods:
    --------
    __init__():
        Initializes the GeminiAPI instance, reads the API key from a file, and configures the generative model.
    chat(texto: str) -> str:
        Generates content based on the input text and returns the generated response.
    """
    def __init__(self):
        load_dotenv()
        self.key = os.getenv('GEMINI_API')
        self.cliente = genai.Client(api_key=self.key)
        self.chat_instance = self.cliente.chats.create(model="gemini-2.0-flash")
        self.contador = 0
        self.basicPrompt = """
            Eres un ChatBot que responde preguntas sobre fisica, para estudiantes de educacion media y universitarios.
            Si ellos pregunta como se resuelve el ejercicio usted tienen que dar hasta 3 pistas para que ellos intenten po si mismo.
            despues de eso usted puede dar la respuesta pero explicada paso a paso.
            El formato de sus respuestas debe ser texto plano, no nescesita formatacion MD y ni HTML.
            Si quieres responder la pregunta por topicos utilize apenas el # y ##. o la lista numerada (1. 2. 3.)
            """

    def generate_response(self, texto):
        if not self.contador%5:
            self.chat_instance.send_message(self.basicPrompt)
            self.contador = 0
        response = self.chat_instance.send_message(texto)
        self.contador += 1
        return response.text
    