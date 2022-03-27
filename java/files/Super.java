// class Super{
//     int a = 10; 
// }

// class B extends Super{
//     int a = 20; 

//     void show(int a){
//         System.out.println(a); // local variable
//         System.out.println(this.a); // current class instance variable
//         System.out.println(super.a); // parent class instance variable
//     }

//     public static void main(String[] args){
//         B b = new B();
//         b.show(30);
//     }
// }


class Super{
    void m1(){
        System.out.println("this is m parent class");
    }
}

class B extends Super{

    void m1(){
        System.out.println("this is m class");
    }

    void show(){
        m1();
        super.m1();
    }

    public static void main(String[] args){
        B b = new B();
        b.show();
    }
}



