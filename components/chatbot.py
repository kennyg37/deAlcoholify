import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dash import html, dcc, Input, Output, State

# Load dataset
data = [
    {"question": "What are some effective ways for young people to reduce or avoid alcohol consumption?", "answer": "Effective ways include joining social groups that don't focus on alcohol, setting personal goals, learning refusal skills, and finding healthy activities like sports or hobbies."},
     {"question": "How does alcohol negatively impact the developing brain in adolescents and young adults?", "answer": "Alcohol can harm brain development in youth, affecting memory, decision-making, and emotional regulation."},
    {"question": "What are some healthy activities or hobbies that can replace drinking alcohol in social settings?", "answer": "Some healthy alternatives include sports, arts, music, volunteering, and fitness activities that promote a positive lifestyle."},
    {"question": "Why is it important for young people to understand the risks associated with drinking alcohol?", "answer": "Understanding risks helps youth make informed choices, avoid health issues, and maintain better mental health."},
    {"question": "How does avoiding alcohol benefit a young person’s physical health?", "answer": "Avoiding alcohol lowers the risk of liver problems, improves sleep, boosts energy, and promotes overall wellness."},
    {"question": "What are the potential long-term benefits of staying alcohol-free during youth?", "answer": "Long-term benefits include a reduced risk of addiction, better mental health, improved academic or career success, and healthier relationships."},
    {"question": "How can friends support each other in reducing alcohol consumption?", "answer": "Friends can create a supportive environment by suggesting non-alcoholic activities, being understanding, and helping resist peer pressure."},
    {"question": "What are some ways to handle peer pressure related to drinking?", "answer": "Handling peer pressure involves practicing refusal skills, finding supportive friends, and standing firm on personal values and health goals."},
    {"question": "How does alcohol affect academic performance?", "answer": "Alcohol can impair concentration, memory, and decision-making, leading to poor academic performance and decreased motivation."},
    {"question": "Why is it important to raise awareness about the effects of alcohol on youth?", "answer": "Raising awareness helps youth understand health risks, make better choices, and reduces the overall prevalence of underage drinking."},
    {"question": "What role can parents play in preventing alcohol use among youth?", "answer": "Parents can educate, set clear rules, be role models, and maintain open communication to guide youth toward healthy choices."},
    {"question": "How does reducing alcohol consumption positively impact mental health?", "answer": "Reducing alcohol improves mental clarity, reduces anxiety and depression risks, and promotes emotional stability."},
    {"question": "What are the social benefits of choosing to stay alcohol-free?", "answer": "Social benefits include forming genuine friendships, building trust, and avoiding situations that could lead to risky behavior."},
    {"question": "How can schools support alcohol prevention among students?", "answer": "Schools can provide educational programs, counseling, and promote activities that raise awareness and offer alternatives to drinking."},
    {"question": "What are some myths about alcohol that young people should be aware of?", "answer": "Common myths include the belief that drinking makes one look 'cool' or that it helps with stress; in reality, it often leads to more problems."},
    {"question": "How can youth influence their peers to avoid alcohol?", "answer": "Youth can be positive role models, speak openly about the risks, and suggest enjoyable, healthy activities to their peers."},
    {"question": "What are the dangers of binge drinking for young people?", "answer": "Binge drinking can lead to alcohol poisoning, risky behavior, long-term health issues, and increased risk of addiction."},
    {"question": "Why is it beneficial for young people to have clear goals related to health and well-being?", "answer": "Clear goals help youth stay focused, make healthier choices, and avoid behaviors that could jeopardize their future."},
    {"question": "How can participating in sports help youth avoid alcohol?", "answer": "Sports require focus, discipline, and physical health, which helps youth stay committed to a healthy lifestyle and avoid substances like alcohol."},
    {"question": "What should young people know about the impact of alcohol on relationships?", "answer": "Alcohol can negatively affect relationships, leading to misunderstandings, conflicts, and trust issues."},
    {"question": "Ni izihe nzira z'ingenzi urubyiruko rushobora gukoresha mu kugabanya cyangwa kwirinda kunywa inzoga?", "answer": "Inzira z'ingenzi zirimo kwifatanya n'itsinda ridakunda inzoga, kwishyiriraho intego, kwiga uburyo bwo kwihagararaho, no gushaka ibikorwa bifite akamaro nko siporo cyangwa umuziki."},
    {"question": "Inzoga zangiza gute ubwonko buri gukura mu rubyiruko?", "answer": "Inzoga zangiza ubwonko bw'urubyiruko, zigira ingaruka ku bwibone, gufata ibyemezo, no kugenga amarangamutima."},
    {"question": "Ni izihe gahunda nziza cyangwa ibikorwa urubyiruko rushobora gukora aho gusangira inzoga?", "answer": "Ibikorwa bifite akamaro birimo siporo, ubuhanzi, umuziki, ibikorwa by'urukundo n'ibindi byafasha kubaho neza."},
    {"question": "Kuki ari ngombwa ko urubyiruko rumenya ingaruka zishobora guterwa no kunywa inzoga?", "answer": "Kumenya ingaruka bifasha urubyiruko gufata ibyemezo biboneye, kwirinda ibibazo by’ubuzima, no kugira intego nziza mu buzima."},
    {"question": "Kwirinda inzoga bifasha gute umubiri w'urubyiruko?", "answer": "Kwirinda inzoga bigabanya ibyago byo kurwara umwijima, bikarinda indwara zitandukanye, ndetse bigatuma umuntu agira ubuzima buzira umuze."},
    {"question": "Ni izihe nyungu z'igihe kirekire umuntu agira mu kwirinda inzoga?", "answer": "Kwiyirinda inzoga bifite inyungu zirimo kugabanya ibyago byo kuba imbata, kugira ubuzima bwiza bwo mu mutwe, no kunoza imibanire n’abandi."},
    {"question": "Inshuti zishobora gute gufashanya kugabanya kunywa inzoga?", "answer": "Inshuti zishobora gufasha gutanga inama z’ubuzima bwiza, kwirinda igitutu cy’abandi, no gusangira ibikorwa bifite akamaro."},
    {"question": "Ni ubuhe buryo urubyiruko rukoreshwa mu guhangana n'igitutu cyo kunywa inzoga?", "answer": "Kwiga uburyo bwo kwanga, gukorana n'inshuti zidatera igitutu, no kwihagararaho ku byemezo bifitiye umuntu akamaro ni inzira nziza."},
    {"question": "Inzoga zigira izihe ngaruka ku myigire?", "answer": "Inzoga zigabanya ubushobozi bwo kwibuka no gufata ibyemezo, bikaba bishobora kwangiza imitsindire y’umunyeshuri."},
    {"question": "Ni gute kumenyekanisha ingaruka z'inzoga ku rubyiruko bifasha?", "answer": "Bifasha urubyiruko kumva akamaro ko kwirinda inzoga, bakarushaho gufata ibyemezo byiza no kugabanya kunywa inzoga batarageza imyaka y’ubukure."},
    {"question": "Ababyeyi bakora iki kugira ngo bafashe abana kwirinda inzoga?", "answer": "Ababyeyi bashobora kuganiriza abana, kubabera urugero rwiza, no gushyiraho amategeko afasha umwana kugendera ku muco mwiza."},
    {"question": "Kugabanya inzoga bifasha gute ubuzima bwo mu mutwe?", "answer": "Kugabanya inzoga bituma umuntu arushaho kugira ibitekerezo bisobanutse, bikagabanya ibyago byo kwigunga no kugira agahinda kenshi."},
    {"question": "Ni izihe nyungu z'imibanire nziza umuntu yageraho mu kwirinda inzoga?", "answer": "Guhitamo kutanywa inzoga bifasha kugira inshuti z’ukuri, kubaha abandi, no kwirinda ibishobora guteza ibibazo mu mibanire."},
    {"question": "Ibigo by'amashuri bishobora gute gufasha mu kurwanya inzoga mu banyeshuri?", "answer": "Amashuri ashobora kwigisha abanyeshuri ingaruka z’inzoga, gutanga ubujyanama, no guha abanyeshuri amahitamo meza mu bikorwa byabo."},
    {"question": "Ni iyihe mitekerereze ibinyoma urubyiruko rukwiye kumenya ku bijyanye n'inzoga?", "answer": "Ibinyoma bikunze kubaho ni nk’uko kunywa inzoga byatuma umuntu asa neza cyangwa bimuha amahoro; nyamara akenshi byongera ibibazo."},
    {"question": "Urubyiruko rushobora gute kugirira abandi ingaruka nziza yo kwirinda inzoga?", "answer": "Urubyiruko rushobora kuba urugero rwiza, kubwira bagenzi babo ibyiza byo kwirinda inzoga, no kwereka abandi ko hari uburyo bwiza bwo kwinezeza."},
    {"question": "Ni izihe ngaruka zo kunywa inzoga nyinshi ku rubyiruko?", "answer": "Kunywa inzoga nyinshi bishobora gutera ibibazo birimo kwiyahuza, gukora ibikorwa bibi, n'ibyago byo kuba imbata y’inzoga mu buzima bw'igihe kirekire."},
    {"question": "Ni gute urubyiruko rwagira intego zijyanye n’ubuzima bwiza?", "answer": "Intego zifasha urubyiruko kugira icyerekezo, guhitamo inzira nziza, no kwirinda ibikorwa bishobora kubagiraho ingaruka mbi."},
    {"question": "Gukina siporo byafasha gute urubyiruko kwirinda inzoga?", "answer": "Siporo zisaba ubwitonzi no kugira ubuzima bwiza, bityo bigatuma urubyiruko rwiyemeza kutanywa inzoga kugira ngo rube rwitwaye neza muri ibyo bikorwa."},
    {"question": "Urubyiruko rukwiye kumenya iki ku ngaruka z'inzoga ku mibanire?", "answer": "Inzoga zishobora kwangiza imibanire ziteza amakimbirane n'ikizere gike hagati y'abantu."},
    {"question": "Ese inzoga zituma umuntu agira akanyabugabo", "answer": "Oya,! ahubwo zigira ingaruka mbi ku mibiri yacu"},
    {"question": "How is alchol harmful", "answer": "Yes, alcohol can be harmful, especially when consumed in excess, leading to liver damage, brain issues, and heart problems.Oya,! ahubwo zigira ingaruka mbi ku mibiri yacu"},
    {"question": "Hey", "answer": "Hello! How can I help you today?"},
    {"question": "What is your name?", "answer": "I am a chatbot designed to answer questions about alcohol and its effects on health."},
    {"question": "What are the effects of alcohol on the body?", "answer": "Alcohol can affect the brain, liver, heart, and other organs, leading to health issues like liver disease, heart problems, and an increased risk of certain cancers."},
    {"question": "Bite?", "answer": "Ni byiza, nagufasha iki?"},
    {"question": "Witwa nde?", "answer": "Ndi chatbot iganira nawe ikagusubiza ibibazo byawe ku bijyanye n'inzoga n'ingaruka zazo ku buzima."}
]
df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(df['question'])

def get_answer(user_question):
    user_question_vector = vectorizer.transform([user_question])
    
    similarities = cosine_similarity(user_question_vector, question_vectors)
    
    best_match_index = similarities.argmax()
    return df.iloc[best_match_index]['answer']

def create_chatbot():
    return html.Div([
        html.Button(
            "Chat",
            id="open-chatbot",
            className="fixed bottom-5 right-5 bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-full shadow-lg z-50"
        ),
        
        html.Div(
            id="chatbot-container",
            className="fixed bottom-20 right-5 bg-gray-900 w-80 h-124 shadow-lg rounded-lg overflow-hidden hidden z-50 border-4 border-gray-800",
            children=[
                html.Div(
                    "Chatbot",
                    className="bg-blue-500 text-white font-bold p-3"
                ),
                html.Div(
                    id="chat-content",
                    className="p-3 overflow-y-auto h-64"
                ),
                html.Div(
                    className="p-3 border-t",
                    children=[
                        dcc.Input(
                            id="user-input",
                            type="text",
                            placeholder="Type your question...",
                            className="w-full px-3 py-2 border rounded"
                        ),
                        html.Button(
                            "Send",
                            id="send-button",
                            className="mt-2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                        )
                    ]
                )
            ]
        )
    ])

def register_callbacks(app):
    @app.callback(
        Output('chatbot-container', 'className'),
        [Input('open-chatbot', 'n_clicks')],
        [State('chatbot-container', 'className')]
    )
    def toggle_chatbot(n_clicks, class_name):
        if n_clicks:
            if 'hidden' in class_name:
                return class_name.replace('hidden', '')
            else:
                return class_name + ' hidden'
        return class_name

    @app.callback(
        Output('chat-content', 'children'),
        [Input('send-button', 'n_clicks')],
        [State('user-input', 'value'), State('chat-content', 'children')]
    )
    def update_chat(n_clicks, user_input, chat_content):
        if chat_content is None:
            chat_content = []

        if n_clicks and user_input:
            chat_content.append(html.Div(f'User: {user_input}', className="my-2 p-2 bg-gray-100 rounded"))
            response = get_answer(user_input)
            chat_content.append(html.Div(f'Bot: {response}', className="my-2 p-2 bg-blue-100 rounded"))
            
            return chat_content
        return chat_content


def chatbot_button():
    return html.Button(
        "Chat",
        id="open-chatbot",
        className="fixed bottom-5 right-5 bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-full shadow-lg z-50"
    )