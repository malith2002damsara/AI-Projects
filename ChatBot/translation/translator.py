import os
import requests
from dotenv import load_dotenv
from logger import setup_logger

load_dotenv()
logger = setup_logger(__name__)


def translate_to_sinhala(text: str) -> str:
    """
    Translate text to Sinhala using Google Translate API
    
    Args:
        text: Text to translate
        
    Returns:
        Translated text (returns original if translation fails)
        
    Raises:
        ValueError: If API key is not configured
    """
    api_key = os.getenv("GOOGLE_TRANSLATE_API_KEY")
    
    if not api_key:
        logger.warning("GOOGLE_TRANSLATE_API_KEY not found in .env file")
        logger.info("Translation skipped - returning original text")
        return text

    if not text or not text.strip():
        logger.warning("Empty text provided for translation")
        return text

    try:
        url = "https://translation.googleapis.com/language/translate/v2"
        payload = {
            "q": text,
            "target": "si",
            "format": "text",
            "key": api_key
        }

        logger.debug(f"Sending translation request (text length: {len(text)} chars)")
        response = requests.post(url, data=payload, timeout=30)

        if response.status_code == 200:
            translated = response.json()["data"]["translations"][0]["translatedText"]
            logger.info("✅ Translation successful")
            return translated
        else:
            logger.error(f"Translation API error (status {response.status_code}): {response.text}")
            logger.info("Returning original text due to API error")
            return text
            
    except requests.exceptions.Timeout:
        logger.error("Translation request timed out after 30 seconds")
        return text
    except requests.exceptions.RequestException as e:
        logger.error(f"Network error during translation: {e}")
        return text
    except (KeyError, IndexError) as e:
        logger.error(f"Unexpected API response format: {e}")
        return text
    except Exception as e:
        logger.error(f"Unexpected error during translation: {e}")
        return text


def translate_response(response_data: dict, extract_answer_fn) -> dict:
    """
    Translate the answer portion of a response to Sinhala
    
    Args:
        response_data: Response dictionary containing answer
        extract_answer_fn: Function to extract answer from response
        
    Returns:
        Response data with translated answer
    """
    if not isinstance(response_data, dict):
        logger.warning("Response data is not a dictionary, skipping translation")
        return response_data
    
    try:
        answer = extract_answer_fn(response_data)
        
        if not answer:
            logger.warning("No answer found to translate")
            return response_data
            
        logger.info("Starting translation to Sinhala...")
        sinhala_answer = translate_to_sinhala(answer)
        response_data["answer"] = sinhala_answer
        
        return response_data
        
    except Exception as e:
        logger.error(f"Error in translate_response: {e}")
        logger.info("Returning original response without translation")
        return response_data