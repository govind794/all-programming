public class MVerloading{

    void show(){
        System.out.println("1");
    }

    void show(int a){
        System.out.println("2");
    }

    public static void main(String[] args){
        MVerloading t = new MVerloading();
        t.show(1);
    }
}