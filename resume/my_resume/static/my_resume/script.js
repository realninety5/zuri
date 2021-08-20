
document.querySelector('.skill').addEventListener('click', () => display('skill'));
document.querySelector('.about').addEventListener('click', () => display('about'));
document.querySelector('.education').addEventListener('click', () => display('education'));
document.querySelector('.experience').addEventListener('click', () => display('experience'));

function display(value){
    document.querySelector('#text-area').textContent = '';
    fetch(`${value}`).then(res => res.json()).then(
        results => {if(value == 'about'){
            document.querySelector('#text-area').textContent = results['body'];
        } else if(value == 'skill'){
            results.forEach(
                result => {
                    let div = document.createElement('div');
                    div.innerHTML = '<b>'+result['name']+'</b>' + ': ' + result['skill_set'];
                    document.querySelector('#text-area').appendChild(div)
                }
            )
        } else if(value == 'experience'){
            let div_jobs = document.createElement('div');
            let div_per = document.createElement('div');
            let title = document.createElement('h2');
            title.innerHTML = "Personal Projects";
            div_per.appendChild(title);
            results.forEach(
                result => {
                  
                    let h2 = document.createElement('h2');
                    h2.innerHTML = result['position'];
                    let loc_com = document.createElement('span')
                    loc_com.innerHTML = result['compro'] + ', ' + result['location'];
                    let date = document.createElement('span')
                    date.innerHTML = '     ' + result['date_start'] + ' - ' + result['date_stop'];
                    if (result['comp'] == false){
                        result['compro'] = '';
                        result['location'] = '';
                        loc_com.innerHTML = '';
                    }
                    let work = document.createElement('ul');
                    result['exp'].forEach(exp => {
                        let done = document.createElement('li')
                        done.innerHTML = '<li>' + exp + '</li>';
                        work.appendChild(done)
                    });
                    div_jobs.appendChild(h2);
                    div_jobs.appendChild(loc_com);
                    div_jobs.appendChild(date);
                    div_jobs.appendChild(work);
                    document.querySelector('#text-area').appendChild(div_jobs)
                }
            )
        } else if (value == 'education'){
            let edu = document.createElement("ul")
            results.forEach( result => {
                let sch = document.createElement('li');
                sch.innerHTML = result['school'] + ', ' + result['course'];
                edu.appendChild(sch)
            })
            document.querySelector('#text-area').appendChild(edu)
        }
    })
}

document.addEventListener('DOMContentLoaded', function(){
    fetch('about').then(
        res => res.json()).then(
            result => {
                document.querySelector('#text-area').textContent = result['body'];
            }
        )
})

document.querySelector('.btnn').addEventListener('submit', (e) => {
    e.preventDefault();
    let email = document.querySelector('#email')
    let subject = document.querySelector('#subject')
    let body = document.querySelector('#body')
    fetch('contact/', {
        method: 'POST',
        body: JSON.stringify({
            email: email.value,
            subject: subject.value,
            body: body.value
        })
    }).then(res => res.json()).then(result => {console.log(result)})
    email.value = '';
    subject.value = '';
    body.value = '';
    document.querySelector('.sent').innerHTML = '<span style="color: green;">Message Sent</span>';
    setTimeout(() => {
        document.querySelector('.sent').innerHTML = '';
    }, 3000);

})