import nltk
from nltk.chat.util import Chat, reflections

# Define the chat patterns and responses
pairs = [
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", "Hi"]
    ],
    [
        r"what is osteoarthritis|osteoarthritis",
        ["Osteoarthritis is a degenerative joint disease that affects the cartilage in joints, causing pain and stiffness."]
    ],
    [
        r"what are the symptoms of osteoarthritis(.*)",
        ["The symptoms of osteoarthritis include joint pain, stiffness, swelling, and reduced range of motion."]
    ],
    [
        r"what causes osteoarthritis(.*)",
        ["Osteoarthritis can be caused by aging, joint injury, obesity, and genetic factors."]
    ],
    [

        r"what are the treatment options for osteoarthritis(.*)",
        ["Treatment options for osteoarthritis include medication, physical therapy, weight loss, and surgical interventions."]
    ],
    [
        r"what lifestyle recommendations can help with osteoarthritis(.*)",
        ["Lifestyle recommendations for osteoarthritis include regular exercise, maintaining a healthy weight, and using joint protection techniques."]
    ],
    [
        r"my case is normal",
        ["For mild osteoarthritis, focus on lifestyle changes like a balanced diet and gentle exercise such as walking or swimming. Over-the-counter pain relievers may help with occasional discomfort, but consult a healthcare provider first. Consider physical therapy for personalized exercises, and protect your joints during daily activities. Monitor your condition with regular checkups, and consult a healthcare professional for guidance."]
    ],
    [
         r"my case is Doubtful",
        ["For moderate osteoarthritis, it's crucial to seek immediate consultation with a healthcare professional for a personalized treatment plan, including prescription medications or injections. Emphasize physical therapy for joint function improvement, weight management to reduce strain, and the use of assistive devices. Encourage a healthy lifestyle, including diet and low-impact exercise. Regular monitoring and potential surgical evaluation may be necessary, so maintain close communication with your healthcare provider."]
    ],
    [
         r"my case is Mild",
        ["For mild osteoarthritis, focus on a balanced lifestyle with exercise like walking or swimming and maintaining a healthy diet. Over-the-counter pain relievers can help with occasional discomfort, but consult a healthcare provider before prolonged use. Practice joint protection in daily activities and consider assistive devices if necessary. Stay active to keep joints mobile, and schedule regular check-ins with a healthcare provider for monitoring and personalized advice."]
        ],
    [
         r"my case is Moderate",
        ["For moderate osteoarthritis, immediate consultation with a healthcare professional is essential. They can create a personalized treatment plan, which may involve prescription medications, physical therapy, and assistive devices. Emphasize maintaining a healthy weight, following a balanced lifestyle, and using pain management techniques under medical supervision. Regular follow-up appointments are crucial to monitor progress and make treatment adjustments. Consider joining support groups for additional emotional and informational support."]
    ],
    [
         r"my case is Severe",
        ["For severe osteoarthritis, immediate consultation with a specialized healthcare professional is critical to discuss treatment options, including surgery or advanced interventions. Focus on comprehensive pain management under medical supervision. Adapt daily routines, explore mobility aids, and engage in prescribed rehabilitation and physical therapy. Seek emotional support through support groups or counseling to address the challenges associated with severe osteoarthritis. Your healthcare provider will guide you towards the most suitable treatment plan.i"]
    ]
]

# Create a chat bot using the defined patterns and responses
chatbot = Chat(pairs, reflections)

print(chatbot.respond('hello'))
