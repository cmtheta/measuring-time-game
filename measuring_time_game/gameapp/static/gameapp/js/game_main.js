{
    'use strict';

    let target = document.getElementById('target');
    let btn = document.getElementById('button');
    let result = document.getElementById('result');
    let record = document.getElementById('record');
    let target_time = document.getElementById('target_time');
    let startTime;
    let targetTime;
    let isStarted = false;

    targetTime = 5.000;
    target.textContent = targetTime.toFixed(3);
    target_time.value = targetTime.toFixed(3);
    console.log(targetTime.toFixed(3));

    btn.textContent = "Start";

    btn.addEventListener('click',function(){
        if(isStarted){
            isStarted = false;
            stop();
        } else {
            isStarted = true;
            start();
        }
    });

    function stop(){
        btn.textContent = "Start";
        let elapsedTime = (Date.now() - startTime) / 1000;
        result.textContent = elapsedTime;
        record.value = elapsedTime;
        document.form.submit();
    }

    function start(){
        btn.textContent = "Stop";
        startTime = Date.now();
        result.textContent = "";
    }

}