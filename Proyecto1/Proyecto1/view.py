from django.http import HttpResponse
import datetime

def saludo(request):

    documento = """
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Meu programa</title>
        </head>
        <body>
            <!-- // Usar as tags dps -->
            <div id="divisao_1" class="animated-element-left">
                <h1>Documentação:</h1>
                <h2>Usando onclick </h2>
                

                <br>
                <p1>o evento onclick chama a nossa função em JS dentro das tags script.</p1>
                <p2>Isso ocorré quando o usuário clicar no botão! </p2>

                <br>
                <p3>Quando você usa innerHTML em um elemento HTML,</p3>
                <p4>você pode obter o conteúdo HTML dentro desse elemento na página.</p4>
                <p5>Aqui está um exemplo básico de como usar innerHTML com JS.</p5>
                <br>
                <p5>Código fonte:</p5>
                <br>
            </div>
            
            <div id="divisao_2" class="animated-element-right">
                <p5 style="margin-top: 10%; padding-left: 10px; color: green">function</p5>
                <p5 style="padding-left: 1px; color: blue"> myFunction()</p5>{
                <br>
                <p5 style="margin-top: 10%; padding-left: 30px;">document.</p5>
                <p5 style="color: purple">getElementById</p5><p5 sytle="yellow">("demo")</p5>
                <p5>.innerHTML = </p5>
                <p5 style="padding: 1px; color:yellow">"Hello World"</p5>;
                <br>
                <p5 style="margin-top: 10%; padding-left: 10px;">}</p5>
                <br>

                <button  id="botao_demonstracao" onclick="hello_world()">
                    Click me
                </button>
                <br>
                <button onclick="refresh_page()" id="botao_demonstracao_2">
                    Refresh
                </button>
            </div>

            <script>
                // Criando a função que mostrará o texto na página
                function hello_world() {
                    document.getElementById("botao_demonstracao").innerHTML = "CLICKED!";
                }

                function refresh_page() {
                    // Função própria do JavaScript para dar um refresh na tela
                    location.reload()
                }
            </script>

            <style>
                body {
                    background-color: black;
                    color: white;
                }

                #divisao_1 {
                    display: grid;
                    place-items: center;
                }

                #divisao_2 {
                    padding-left: 35%;
                }

                #botao_demonstracao_2:hover {
                    scale: 1.3;
                }

                #botao_demonstracao:hover {
                    scale: 1.3;
                }

                #botao_demonstracao_2 {
                    border-radius: 3%;
                    border-color: white;
                    margin-top: 1%;
                    background-color: lightblue;
                    color: blue; 
                    margin-left: 200px;
                    display: grid;
                    place-items: center;
                }

                #botao_demonstracao {
                    border-radius: 3%;
                    border-color: white;
                    background-color: lightblue;
                    color: blue;
                    margin-left: 200px;
                    margin-top: 10%;
                    display: grid;
                    place-items: center;
                }

                @keyframes slideInFromRight {
                    0% {
                        transform: translateX(100%);
                    }
                    100% {
                        transform: translateX(0);
                    }
                }

                @keyframes slideInFromLeft {
                    0% {
                        transform: translateX(-100%);
                    }
                    100% {
                        transform: translateX(0);
                    }
                }

                .animated-element-left {
                    animation: slideInFromLeft 1s ease-in;
                }
                
                .animated-element-right {
                    animation: slideInFromRight 1s ease-in;
                }
            </style>
        </body>
        </html>""" 
    

    return HttpResponse(documento)


def fecha(request):

    tiempo = datetime.datetime.now()

    return HttpResponse("""

    <html>
    <body>
    <h1> 
    fecha y hora %s
    </h1>
    </body>
    </html>

""" %tiempo)