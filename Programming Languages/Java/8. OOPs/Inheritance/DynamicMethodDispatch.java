class ProgrammingLanguage{
    protected String type;
    protected int launching;
    protected String name;

    ProgrammingLanguage(){
        System.out.println("Programming languages are the medium to communicate with computers which understand only binary(0 and 1)");
    }

    public void name(){
        System.out.println("I am a Programming Language");
    }

    public void get(){
        System.out.println("Name : "+name);
        System.out.println("Type : "+type);
        System.out.println("Launching : "+launching);
    }
}

class CLanguage extends ProgrammingLanguage{
    CLanguage(){
       type = "Procedural Oriented Programing";
       launching = 1973;
       name = "C Programming Language";
    }

    public void name(){
        System.out.println("I am C Programming Language");
    }
}
class CPP extends CLanguage{
    CPP(){
       type = "Object Oriented Programing";
       launching = 1985;
       name = "C Plus Plus";
    }

    public void name(){
        System.out.println("I am C++ Programming Language");
    }
}

class Java extends CPP{
    Java(){
        type = "Object Oriented Programing";
        launching = 1996;
        name = "java";
    }

    public void name(){
        System.out.println("I am java Programming Language");
    }
}

public class DynamicMethodDispatch {
    public static void main(String[] args) {
        // Dynamic Method Dispatch - This is used to achieve run time polymorphism

        System.out.println("\nObject of c language");
        ProgrammingLanguage c = new CLanguage();    // (Reference of ProgrammingLanguage class and object of CLanguage class)
        c.name();    // rum name method of CLanguage class
        c.get();    // rum get method for CLanguage class which values will set constructor of CLanguage

        System.out.println("\nObject of c++ language");
        CLanguage cpp = new CPP();    // (Reference of CLanguage class and object of CPP class)
        cpp.name();      // rum name method of CPP class
        cpp.get();      // rum get method for CPP class which values will set constructor of CPP

        System.out.println("\nObject of java language");
        CPP java = new Java();    // (Reference of CPP class and object of Java class)
        java.name();     // rum name method of Java class
        java.get();     // rum get method for Java class which values will set constructor of Java
    }
}
