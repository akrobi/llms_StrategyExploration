import sys
import os

import cohere

sys.path.append(os.path.abspath(os.path.join('..')))
from dotenv import load_dotenv

api_key = os.getenv('COHERE_APIKEY_JDENTITIES')

co = cohere.Client(api_key)
response = co.generate(
  model='xlarge',
  prompt='Company: Casper\nProduct Name: The Wave Hybrid\nWhat is it: A mattress to improve sleep quality\nWhy is it unique: It helps with back problems\nDescription: We\'ve got your back. Literally, improving the quality of your sleep is our number one priority. We recommend checking out our Wave Hybrid mattress as it is designed specifically to provide support and pain relief.\n--SEPARATOR--\nCompany: Glossier\nProduct Name: The Beauty Bag\nWhat is it: A makeup bag\nWhy is it unique: It can hold all your essentials but also fit into your purse\nDescription: Give a very warm welcome to the newest member of the Glossier family - the Beauty Bag!! It\'s the ultimate home for your routine, with serious attention to detail. See the whole shebang on Glossier.\n--SEPARATOR--\nCompany: Cohere\nProduct Name: The FastMile\nWhat is it: A running shoe\nWhy is it unique: It\'s designed for long-distance running\nDescription:',
  max_tokens=50,
  temperature=0.9,
  k=0,
  p=0.75,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=["--SEPARATOR--"],
  return_likelihoods='NONE')
print('Prediction: {}'.format(response.generations[0].text))
x = response.generations[0].text
# remove --SEPARATOR-- if x contains it
if '--SEPARATOR--' in x:
  x = x.replace('--SEPARATOR--', '')

# trim the sentence x
x = x.strip()