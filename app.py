from flask import Flask, render_template, request
import openai

app = Flask(__name__)


openai.api_key = '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'

@app.route('/', methods=['GET', 'POST'])
def translate_text():
    translated_result = None

    if request.method == 'POST':
        text = request.form['text']
        source_lang = request.form['source_lang']
        target_lang = request.form['target_lang']
        
        prompt = f"Translate the following text from {source_lang} to {target_lang}:\n{text}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        
        translated_result = response.choices[0].text.strip()

    return render_template('index.html', translated_result=translated_result)

if __name__ == '__main__':  
    app.run(debug=True)
