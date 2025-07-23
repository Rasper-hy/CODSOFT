let user = null;
let quizList = [];
try {
  const stored = localStorage.getItem('quizList');
  if (stored){
    quizList = JSON.parse(stored);
  }
} catch (e) {
  console.error("Invalid JSON in quizList:",e);
  quizList = [];
}
let state = 'home';
let currentQuizIndex = 0;
let userAnswers = [];

function render() {
  const m = document.getElementById('main');

  if (state === 'home') {
    m.innerHTML = `
      <h2>🎪 The Quiz Carnival 🎪</h2>
      ${user ? `
        <p>Welcome back, <strong>${user}</strong>!</p>
        <button onclick="user=null; render()">Logout</button><br>
      ` : `
        <button onclick="state='auth'; render()">Login</button><br>
      `}
      <button onclick="state='create'; render()">Create a Quiz</button>
      <button onclick="state='list'; render()">Take a Quiz</button>
    `;
  }

  else if (state === 'auth') {
    m.innerHTML = `
      <h3>Login</h3>
      <input id="u" placeholder="Enter your name"><br>
      <button onclick="user=document.getElementById('u').value.trim(); state='home'; render()">Login</button>
      <button onclick="state='home'; render()">Back</button>
    `;
  }

  else if (state === 'create') {
    if (!user) { state = 'auth'; render(); return; }
    m.innerHTML = `
      <h3>Create Your Quiz</h3>
      <input id="t" placeholder="Quiz Title"><br>
      <div id="qs"></div>
      <button onclick="addQuestion()">Add Question</button>
      <button onclick="saveQuiz()">Save Quiz</button>
      <button onclick="state='home'; render()">Back</button>
    `;
    window.qarr = [];
    addQuestion();
  }

  else if (state === 'list') {
    m.innerHTML = `
      <h3>Available Quizzes</h3>
      ${!quizList.length ? 'No quizzes available yet.' : quizList.map((q, i) => `
        <div>
          ${q.t} | by ${q.u}
          <button onclick="currentQuizIndex=${i}; userAnswers=[]; state='take'; render()">Take</button>
        </div>
      `).join('')}
      <button onclick="state='home'; render()">Back</button>
    `;
  }

  else if (state === 'take') {
    const qz = quizList[currentQuizIndex];
    const q = userAnswers.length;
    m.innerHTML = `
      <h3>${qz.t}</h3>
      <p><strong>${qz.qs[q].q}</strong></p>
      ${qz.qs[q].o.map((o, i) => `
        <label>
          <input type="radio" name="a" value="${i}" ${i === 0 ? 'checked' : ''}>
          ${o}
        </label><br>
      `).join('')}
      <button onclick="
        userAnswers.push(Number(document.querySelector('[name=a]:checked').value));
        if (userAnswers.length === qz.qs.length) state='finish';
        render();
      ">Next</button>
    `;
  }

  else if (state === 'finish') {
    const qz = quizList[currentQuizIndex];
    let score = 0;
    m.innerHTML = `<h3>Quiz Results</h3><ol>`;
    qz.qs.forEach((q, i) => {
      const correct = q.a === userAnswers[i];
      if (correct) score++;
      m.innerHTML += `
        <li>
          ${q.q}<br>
          Your Answer: ${q.o[userAnswers[i]] || '-'} ${correct ? '✔️' : '❌'}<br>
          Correct Answer: <strong>${q.o[q.a]}</strong>
        </li>
      `;
    });

    let feedback = score === qz.qs.length ? "🎉 Perfect Score!" :
                   score >= qz.qs.length / 2 ? "👍 Good effort!" :
                   "💡 Better luck next time!";
    m.innerHTML += `</ol>
      <strong>Score: ${score} / ${qz.qs.length}</strong><br>
      <p style="font-size:1.2em">${feedback}</p>
      <button onclick="state='list'; render()">Back to Quizzes</button>
      <button onclick="state='home'; render()">Home</button>
    `;
  }
}

function addQuestion() {
  const n = window.qarr.length;
  const div = document.getElementById('qs');
  window.qarr.push({ q: '', o: ['', '', '', ''], a: 0 });
  div.innerHTML += `
    <input placeholder="Question ${n + 1}" oninput="window.qarr[${n}].q=this.value"><br>
    ${[0, 1, 2, 3].map(i => `
      <label>
        <input type="radio" name="c${n}" value="${i}" ${i === 0 ? 'checked' : ''}
          onclick="window.qarr[${n}].a=${i}">
        <input placeholder="Option ${i + 1}" oninput="window.qarr[${n}].o[${i}]=this.value">
      </label><br>
    `).join('')}
    <hr>
  `;
}

function saveQuiz() {
  const title = document.getElementById('t').value.trim();
  const questions = window.qarr.filter(q => q.q && q.o.every(opt => opt.trim()));
  if (!title || !questions.length) return alert("Please fill out all fields!");
  quizList.push({ t: title, u: user, qs: questions });
  alert("Your quiz has been saved!");
  state = 'home';
  render();
}
document.addEventListener("DOMContentLoaded",function () {
render();
});