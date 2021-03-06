'use strict';   // 비상식적인 일들 예를 들면 변수선언 안한 변수에 값 추가 등에 에러를 나타내준다. 자바 스크립트 엔진이 더욱 효율적으로 코드를 분석 가능하므로 성능 개선까지 기대됌.

const myName = "김재민";
const greeting = "hello " + myName;
const bye = `Goodbye ${myName}`;
const num1 = '123';
console.log(greeting);
console.log(bye);
console.log(typeof(null));  // A. 왜 null값은 object 타입이지? Q. 버그랍니다.
console.log(parseInt(num1));



switch(myName){         // switch 쓰는법
    case "김재민":
        console.log("My name");
        break;
    case "최진철":
    case "석승환":
        console.log("My friend");
        break;
    default:
        console.log("who are you");
        break;
}



function printAll(...args){         // rest parameter
    for(const arg of args){         // for of
        console.log(arg);
    }
    // return undefined;            // 항상 이 문장이 숨겨져 있다고 보면 됀다.
}
printAll('신', "기", "하", "다");



const add = (a,b) => a+b;                      // arrow function
const multiply = (a,b) => {                    // arrow function, 블럭을 쓸 때는 return을 써줘야 한다.
    console.log(a*b);
    return a*b;
};
console.log(add(1,2));
multiply(2,4);



(function print(){                  // IIFE
    console.log("IIFE");
})();



class User{
    constructor(firstName, lastName){
        this.firstName = firstName;
        this.lastName = lastName;
    }

    get age(){                          // 객체.age를 했을 때 실행되는 함수.
        return this._age;
    }

    set age(value){                     // 객체.age = value 를 했을 때 실행되는 함수. 따라서 _기호를 써서 변수이름을 다르게 안해주면 무한히 setter가 실행되어 오류가 뜸.
        this._age = value < 0 ? 0 : value;
    }
}
const user1 = new User('재민', '김');
user1._age = -1;                        // 이렇게 하면 set 함수를 이용하는 것이 아닌 별도의 property인 _age에 직접 접근해서 넣는 것이라 이렇게 하면 안됌.    
console.log(user1.age);
user1.age = -3;
console.log(user1.age);
user1.age = 10;
console.log(user1._age);            // 실제값은 별도의 property _age에 저장이 된다. 하지만 객체 외부에서 건드리지 않는 것이 관습.\



console.log(user1 instanceof Object);       // 모든 객체들은 Object라는 클래스를 상속받는다.



function printValue(obj, key){
    console.log(obj[key]);              // computed property. 동적으로 key의 value를 받아올때 유용하게 사용한다.
}
printValue(user1, 'firstName');         // key should be always string



function makePerson(name, age){         // property value shorthand
    return {
        name,   // name = name에서 왼쪽은 key값이고 오른쪽은 value값을 parameter로 가져오는 것인데 이것은 생략 가능하고 생략해야 에러가 안뜬다.
        age
    };
}
const user2 = makePerson('김동진', 24);
console.log(user2);



function Person(name, age){             // constructor function
    this.name = name;
    this.age = age;
}
const user3 = new Person('최진철', 23);         // constructor function은 클래스 쓰는 것처럼 쓴다.
console.log(user3);                     // 일반 object들과 출력이 다르다..



console.log('name' in user3);           // in operator



const people = new Array();
const language = ['python', 'JS', 'Java'];
console.log(language[language.length - 1]);



language.forEach(function(value, index, array){         // 배열에서의 forEach
    console.log(value, index, array);
});



function fetchUser(){                                   // Promise producer
    return new Promise((resolve,reject) => {
        // do network request in 10 secs...
        resolve("promise");
    });
}
const practicePromise = fetchUser();
console.log(practicePromise);



async function asyncFetchUser(){    
    // do network request in 10 secs...                // async 사용
    return "promise";
}
const practiceAsyncPromise = asyncFetchUser();
practiceAsyncPromise.then(console.log);                 // then. 비동기적인게 확인가능
console.log(practiceAsyncPromise);
