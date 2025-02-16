# Quiz
HTML code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="cyber.css">
    <link rel="icon" href="https://cdn.prod.website-files.com/63a71c562e3ccbc6f6a40f0f/65bcbb02d38aec8f6ce1f1ab_L%26D_Cyber%26ITSecurity_Hero.png">
    <title>Cybersecurity Quiz Game</title>
</head>
<body>
    <div id="game-container">
        <h2>Cybersecurity Quiz</h2>
        <p id="question"></p>
        <div id="answers"></div>
        <p id="score">Score: 0</p>
    </div>
    <script src="cyber.js"></script>
</body>
</html>


JavaScript code
const questions = [
    {
        question: "What is the best way to protect your password?",
        answers: ["A.Write it down", "B.Share it with a friend", "C.Use a password manager", "D.Use the same password everywhere"],
        correct: 2
    },
    {
        question: "Which is a sign of a phishing email?",
        answers: ["A.An unknown sender", "B.Urgent requests for personal information", "C.Poor grammar and spelling", "D.All of the above"],
        correct: 3
    },
    {
        question: "What should you do if you receive a suspicious link?",
        answers: ["A.Click to see where it goes", "B.Report it and avoid clicking", "C.Forward it to everyone", "D.Ignore it"],
        correct: 3
    },
    {
        question: "What should you do if you receive a spam calls?",
        answers: ["A.Answer the call and give information","B.add to block","C.inform cyber police", " D.Both B&C"],
        correct: 3
    }
];

let currentQuestionIndex = 0;
let score = 0;

function loadQuestion() {
    if (currentQuestionIndex >= questions.length) {
        document.getElementById("game-container").innerHTML = `<h2>Game Over!</h2><p>Your final score is: ${score}</p>`;
        return;
    }
    
    const questionObj = questions[currentQuestionIndex];
    document.getElementById("question").innerText = questionObj.question;
    
    const answersDiv = document.getElementById("answers");
    answersDiv.innerHTML = "";
    
    questionObj.answers.forEach((answer, index) => {
        const btn = document.createElement("button");
        btn.innerText = answer;
        btn.className = "btn";
        btn.onclick = () => checkAnswer(index);
        answersDiv.appendChild(btn);
    });
}

function checkAnswer(selectedIndex) {
    if (selectedIndex === questions[currentQuestionIndex].correct) {
        score++;
    }
    currentQuestionIndex++;
    document.getElementById("score").innerText = `Score: ${score}`;
    loadQuestion();
}

loadQuestion();


CSS code
body {
    font-family: Arial, sans-serif;
    text-align: center;
    background-color: #f4f4f4;
    padding: 20px;
}
#game-container {
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 5px 50px rgba(0, 0, 0, 0.1);
    max-width: 500px;
    margin: auto;
}
.btn {
    display: block;
    width: 100%;
    margin: 10px 0;
    padding: 10px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
.btn:hover {
    background-color: black;
}
