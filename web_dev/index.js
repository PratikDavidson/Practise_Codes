
class Employee{
    
    
    constructor(fname, lname, pay) {
        this.fname = fname
        this.lname = lname
        this.pay = pay
        Employee.num_of_emps++
    }

    get fullname() {
        return this.fname + ' ' + this.lname
    }
    set fullname(name) {
        this.fname = name.split(' ')[0]
        this.lname = name.split(' ')[1]
    }
}

class Developer extends Employee{
    
    constructor(fname, lname, pay, lang) {
        super(fname, lname, pay)
        this.lang = lang
    }
}

class Manager extends Employee{

    constructor(fname, lname, pay, emp = null) {
        super(fname, lname, pay)
        if (emp == null) {
            this.emps = []
        } else {
            this.emps = [emp]
        }
    }

    add_emps(emp) {
        if (emp in this.emps) {
            return
        }
        this.emps.push(emp)
    }

    remove_emps(emp) {
        if (emp in this.emps) {
            this.emps.pop(emp)
        }
    }
    print_emps(emp) {
        for (emp of this.emps) {
            console.log(emp)
        }
    }
}

let emp_1 = new Employee('Pratik', 'Davidson', 50000)
let emp_2 = new Employee('Tim', 'Hudson', 60000)

console.log(emp_1.fullname)
console.log(emp_2.fullname)

let dev_1 = new Developer('Pratik', 'Davidson', 50000, 'Python')
let dev_2 = new Developer('Tim', 'Hudson', 60000 , 'Java')

let mrg = new Manager('Kate', 'Harrington', 100000, dev_1)
mrg.add_emps(dev_2)
mrg.print_emps()
mrg.remove_emps(dev_1)
mrg.print_emps()