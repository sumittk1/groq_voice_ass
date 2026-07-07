from flask import Flask, request, jsonify, render_template
import base64
from groq import Groq

app = Flask(__name__)
# client = Groq()
client = Groq(
    api_key="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"
)

@app.route('/')
def home():
    # Yeh automatically 'templates' folder mein index.html dhoondega
    return render_template('index.html')

@app.route('/api/voice-chat', methods=['POST'])
def voice_chat():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file received"}), 400
        
    audio_file = request.files['audio']
    audio_bytes = audio_file.read()

    # 1. Whisper API (Voice to Text)
    transcription = client.audio.transcriptions.create(
        file=("user_voice.webm", audio_bytes),
        model="whisper-large-v3",
        response_format="json"
    )
    user_text = transcription.text
    # Aapka specific data jo aap AI ko dena chahte hain
    my_custom_data = """
    Main Laboratories in Lakshya 2047Ground Floor LabsSpecialized Labs:GF-01: NVIDIA LabGF-02: Cisco LabGF-03: ABB Lab-1GF-04: Industrial Drives & Control LabGF-04-A: Home Automation LabGF-05: PLC & SCADA LabGF-06: ABB Lab-2GF-08: AR/VR LabNon-Specialized Labs:GF-07: Microsoft LabGF-11: ANSYS LabGF-12: Adobe LabGF-13: Autodesk LabGF-14: VLSI LabGF-15: AWS LabGF-16: Apple LabFirst Floor Labs101: RPTO Operation Setup Lab102: Drone Technician Lab103: Drone Battery System Repair Lab104: Prototyping Zone105: Material Synthesis Zone106: Major Machine Zone107: Minor Machine Zone110: Mind LabManagement & OperationsLakshya 2047 Manager: Located on the Third Floor. Responsible for the overall management of the building and handling GCF Training.Ethnotech Representative: Operates out of the CFS Office (Campus Manager Office) in the Ground Floor Board Room (GF-10). They manage and handle GCF Training.Important Figures & LeadershipDr. Jitendra Singh: Inaugurated the building on May 8, 2026. He serves as the Union Minister of State for Science and Technology, Earth Sciences, and the Prime Minister's Office.  Dr. Devanshu Patel: President of Parul University.Dr. Parul Patel: Vice President (Student Affairs, General Administration, Admissions Committee Chair).Dr. Geetika Madan Patel: Vice President (Quality, Research, Health Sciences), Medical Director, and Managing Trustee.Dr. Komal Patel: Vice President (Medical and Paramedical Health Sciences), Medical Director, and Managing Trustee.Key PartnersParul University: A 250-acre NAAC A++ accredited private university located in Vadodara, Gujarat.NSDC (National Skill Development Corporation): A Public-Private Partnership under the Ministry of Skill Development and Entrepreneurship focusing on national skill development.Ethnotech Academy: A Bengaluru-based skill development and technology training organization that manages training execution and placement support.
    """

    # 2. Llama 3 API (Text to Text Reply) - STRICTLY BOUNDED KNOWLEDGE
    chat_completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system", 
                "content": (
                    "You are Jarvis. You must reply strictly in English.\n\n"
                    "KNOWLEDGE BASE:\n"
                    f"{my_custom_data}\n\n"
                    "CRITICAL RULES:\n"
                    "1. You must ONLY answer questions based on the KNOWLEDGE BASE provided above.\n"
                    "2. If the user asks a question that is NOT covered in the KNOWLEDGE BASE, you must strictly reply with: 'I am not authorized to provide that information, sir.'\n"
                    "3. Do not use outside knowledge or general knowledge. Even if you know the answer to a general question (like 'What is the capital of India?'), refuse to answer it.\n"
                    "4. Keep your answers brief (1 sentence)."
                )
            },
            {"role": "user", "content": user_text}
        ]
    )
    ai_text_reply = chat_completion.choices[0].message.content
    # 3. Orpheus API (Text to Voice)
    audio_response = client.audio.speech.create(
        model="canopylabs/orpheus-v1-english",
        voice="troy", 
        input=ai_text_reply,
        response_format="wav"
    )
    
    out_audio_bytes = audio_response.read()
    audio_base64 = base64.b64encode(out_audio_bytes).decode('utf-8')
    
    return jsonify({
        "user_text": user_text,
        "ai_text": ai_text_reply,
        "audio_base64": audio_base64
    })

if __name__ == '__main__':
    print("Mission Control Auto-Voice starting... Open http://127.0.0.1:5000 in your browser!")
    app.run(debug=True, port=5000)