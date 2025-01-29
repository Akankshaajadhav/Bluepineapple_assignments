class Calculator {
    constructor(number=0) {
        this.number=number;
    }

    add(num){
        this.number+=num;
        return this;
    }

    subtract(num){
        this.number-=num;
        return this;
    }

    multiply(num){
        this.number*=num;
        return this;
    }

    divide(num){
        this.number/=num;
        return this;
    }

    getResult(){
        return this;
    }
}

var calc=new Calculator();
console.log(calc.add(4).subtract(5).multiply(3).divide(2).getResult());
