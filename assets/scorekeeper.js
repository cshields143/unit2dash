const add2score = player => {
  const tbody = document.querySelector('#score-output');
  const trs = tbody.querySelectorAll('tr');
  [...trs].forEach(row => {
    const name = row.firstElementChild.textContent;
    if (name === player) {
      const current = row.firstElementChild.nextElementSibling.textContent;
      const newe = +current + 1;
      row.firstElementChild.nextElementSibling.textContent = newe;
    }
  });
};

document.body.addEventListener('click', ev => {
  const t = ev.target;
  const id = t.id;
  const is_opt = /^opt\-\d\-input$/.test(id);
  if (is_opt) {
    const choice = +(id.split('-')[1]);
    if (choice < 4) {
      const answer_el = document.querySelector('#guess-answer');
      const answer = answer_el.textContent;
      const choice_val = t.textContent;
      answer_el.style.background = 'transparent';
      if (choice_val === answer) add2score('You!');
      const tompred = document.querySelector('#tom-guess-output').textContent;
      const dickpred = document.querySelector('#dick-guess-output').textContent;
      const harrypred = document.querySelector('#harry-guess-output').textContent;
      if (tompred === answer) add2score('Tom');
      if (dickpred === answer) add2score('Dick');
      if (harrypred === answer) add2score('Harry');
      const btns = document.querySelectorAll('#options-output button');
      [...btns].forEach(b => {
        b.disabled = true;
      });
    }
  } else if (id === 'trigger-game-round') {
    const answer_el = document.querySelector('#guess-answer');
    const btns = document.querySelectorAll('#options-output button');
    if (answer_el) {
      answer_el.style.background = 'black';
      [...btns].forEach(b => {
        b.disabled = false;
      });
    }
  } else if (id === 'trigger-score-clear') {
    const tbody = document.querySelector('#score-output');
    const trs = tbody.querySelectorAll('tr');
    [...trs].forEach(el => {
      el.firstElementChild.nextElementSibling.textContent = 0;
    });
  }
});