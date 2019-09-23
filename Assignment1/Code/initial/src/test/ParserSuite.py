import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):


#========================================TEST DECLARATIONS========================================
    def test_var_declaration_1(self):
        input = """int var, var[9];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    def test_var_declaration_2(self):
        input = """void var var, var[9];"""
        expect = "Error on line 1 col 9: var"
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_var_declaration_3(self):
        input = """boolean array[9;"""
        expect = "Error on line 1 col 15: ;"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_var_declaration_4(self):
        input = """string var = "Variable";"""
        expect = "Error on line 1 col 11: ="
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_var_declaration_5(self):
        input = """
                int var0[0], var0;
                float var1[1], var1, var2;
                boolean var2, var2[2];
                string var3, var3[3], var4[];
                """
        expect = "Error on line 5 col 43: ]"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_var_declaration_6(self):
        input = """string main = "That's a keyword dude!";"""
        expect = "Error on line 1 col 12: ="
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_var_declaration_7(self):
        input = """string void = "No, he is not. I am!!!";"""
        expect = "Error on line 1 col 7: void"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_var_declaration_8(self):
        input = """int booIean = "I am legal!!";"""
        expect = "Error on line 1 col 12: ="
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_var_declaration_9(self):
        input = """int var1 var2; float var1var2;"""
        expect = "Error on line 1 col 9: var2"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_var_declaration_10(self):
        input = """int []balance;"""
        expect = "Error on line 1 col 13: ;"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    
    

    def test_fun_declaration_1(self):
        input = """
                int array[000001], var;
                string[] createPointer(int a, boolean b[]){}
                float beHumble(){};
                """
        expect = "Error on line 4 col 34: ;"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    def test_fun_declaration_2(self):
        input = """
                boolean first;
                string createPointer(int a, boolean b[]){
                    {
                        {}
                    }
                }
                float beHumble(){}
                int second;
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    def test_fun_declaration_3(self):
        input = """
                boolean first;
                void createPointer(int a, boolean b[]){
                    int a, b, c;
                    int[] main(){}
                }
                float beHumble(){}
                int second;
                """
        expect = "Error on line 5 col 23: ["
        self.assertTrue(TestParser.checkParser(input,expect,213))
    def test_fun_declaration_4(self):
        input = """
                void _(int _, float _[]){
                    string _[0];
                }
                string[] _(void nothing){
                    //do nothing
                }
                """
        expect = "Error on line 5 col 27: void"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    def test_fun_declaration_5(self):
        input = """
                boolean true_false;
                boolean isTrue(int a, b, c){
                    printf("Yeah you can't declare parameters like that!")
                }
                """
        expect = "Error on line 3 col 38: b"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    def test_fun_declaration_6(self):
        input = """
                boolean true_false;
                boolean isTrue(int a){
                    int right, left;
                    right = true;
                    left = false;
                    {}
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    def test_fun_declaration_7(self):
        input = """
                int life, death;
                boolean[] amILiving(float people[]){
                    printf("There is no answer");
                    return life || death;
                }
                return love;
                """
        expect = "Error on line 7 col 16: return"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    def test_fun_declaration_8(self):
        input = """
                void[] amIEmpty(int a){
                    if(love == 0) 
                        printf("Yes you are!");
                    else
                        printf("There's still something inside you! Stay strong!");
                    return Hollow;
                }
                """
        expect = "Error on line 2 col 20: ["
        self.assertTrue(TestParser.checkParser(input,expect,218))
    def test_fun_declaration_9(self):
        input = """
                void amIEmpty(int a[]){
                    // make your dream come true
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    def test_fun_declaration_10(self):
        input = """
                int[3] function(){
                    // be kind to people
                }
                """
        expect = "Error on line 2 col 20: 3"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    def test_fun_declaration_11(self):
        input = """boolean[] amIEmpty(int a);"""
        expect = "Error on line 1 col 25: ;"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    def test_fun_declaration_12(self):
        input = """
                float[] amIEmpty(int a){
                    if(smile) 
                        difficult = difficult / 2;
                    else
                        difficult = difficult * 2;
                    return Hollow;
                };
                """
        expect = "Error on line 8 col 17: ;"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    def test_fun_declaration_13(self):
        input = """
                void amIEmpty(int a){
                    int[] a(){};
                }
                """
        expect = "Error on line 3 col 23: ["
        self.assertTrue(TestParser.checkParser(input,expect,223))
    def test_fun_declaration_14(self):
        input = """
                void amIEmpty(int a){
                    if(falling)
                        Flying();
                    int var;
                    float var[3];
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    def test_fun_declaration_15(self):
        input = """
                string[] moreThanICanSay(string toYou){
                    printf("I love you!");
                }
                float[] countNumbers(){}
                int var, var1, var2[999];
                boolean var[999], bool[0];
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))
#=================================================================================================





#========================================TEST STATEMENTS========================================
    def test_if_statement_1(self):
        input = """
                void main(){
                    if((life == difficult) || (feeling == depression)){
                        hug = 3000;
                        You = Someone(hug);
                    }
                    else
                        printf("Have a good day!");
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    def test_if_statement_2(self):
        input = """
                void main(){
                    if((life == difficult) || (feeling == depression))
                        if(beHumble())
                            if(beKind())
                                if(bePositive())
                                    believeInTheFuture(you);
                    else
                        printf("Have a good day!");
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    def test_if_statement_3(self):
        input = """
                void main(){
                    if(goDown(floor4))
                        if(goDown(floor3))
                            if(goDown(floor2))
                                if(goDown(floor1))
                                    if(goDown(basement))
                                        printf("Hello Annabelle!");
                                    else
                                        goUp();
                                else
                                    goUp();
                            else
                                goUp();
                        else
                            printf("You shouldn't go to the basement :)))");
                    else

                }
                """
        expect = "Error on line 19 col 16: }"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    def test_if_statement_4(self):
        input = """
                void main(){
                    letMakeAStair(true);
                    if(stair){
                        //do nothing
                    }
                    else
                        if(stair){
                            //do nothing}}}}}}
                        }
                        else
                            if(stair){
                                {// do nothing}
                            }}
                            else{
                                {// do nothing}
                }}}
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    def test_if_statement_5(self):
        input = """
                void main(){
                    chanceOfMeetingYourFutureWife = 0;
                    if(meetSomeone(aGirl)){
                        {
                            {
                                shy(you);
                                runAway(you);
                            }
                        }
                        she = smile("looking at you");
                    }
                    if(meetSomeone(aGirl)){
                        beStrong = true;
                        chanceOfMeetingYourFutureWife = 1;
                    }
                    else
                }
                """
        expect = "Error on line 18 col 16: }"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    def test_if_statement_6(self):
        input = """
                void main(){
                    if(believe == true)
                        stronger = yes;
                        if(kind == true)
                            better = yes;
                            if(fear == no)
                                success = yes;
                    else{
                        cout("Keep fighting!");
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    def test_if_statement_7(self):
        input = """
                void main(){
                    if(1)
                        if(2)
                            if(3)
                                if(4)
                                    if(5)
                    stopSayingIf();
                    action(true);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    def test_if_statement_8(self):
        input = """
                float main(){
                    if(sky)
                        if(sea)
                    else{earth;}
                    else{rain;}
                    if(light)
                    else{dark;}
                    else{//life}
                }
                """
        expect = "Error on line 5 col 20: else"
        self.assertTrue(TestParser.checkParser(input,expect,233))



    def test_do_statement_1(self):
        input = """
                void main(){
                    do{
                        {
                            printf("Easy testcase");
                        }
                    }
                    while(busy == false);

                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    def test_do_statement_2(self):
        input = """
                void main(){
                    do{
                        {
                            printf("Easy testcase");
                        }
                    }
                    While(busy == false);
                    int shitHappens;
                    guessWhatWrongInThisTestcase(viewer);
                }
                """
        expect = "Error on line 9 col 20: int"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    def test_do_statement_3(self):
        input = """
                void main(){
                    int bePatient;
                    do
                    bePatient = 0;
                    bePatient = 1;
                    bePatient = 2;
                    if(bePatient > 3)
                        dontBePatientAnymore(":)");
                    while(mood < usualState);
                    do number1 + number2;
                    while(number1 > number2);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    def test_do_statement_4(self):
        input = """
                void main(){
                    do
                        do
                            do
                                do
                                    tooManyDos("stop");
                                while(free);
                            while(free);
                        while(notFree)
                    while(busy == false);

                }
                """
        expect = "Error on line 11 col 20: while"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    def test_do_statement_5(self):
        input = """
                void main(){
                    do{
                        sitDown;
                        beHumble;
                    }while(living);
                    whiLe(feeling);
                    whiLe(breathing);
                    whIle(youStillCan);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    def test_do_statement_6(self):
        input = """
                void main(){
                    do{
                        anythingYouWant();
                        butNotIllegal();
                    }
                    whiLe(doingSomething);
                    becomeABetterPerson = 1;
                    while(enjoyLife);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    def test_do_statement_7(self):
        input = """
                void main(){
                    do
                    while(thisIsWrong);
                    yeah27436itri2ri434635462!$%^!#$@#$@^!$%^#$;
                }
                """
        expect = "Error on line 4 col 20: while"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    def test_do_statement_8(self):
        input = """
                void main(){
                    do
                        {do
                            do
                                do
                                    DO;
                                while(youStillCan);
                            while(youStillCan);}
                        while(youStillCan);
                    while(youStillCan);

                }
                """
        expect = "Error on line 9 col 47: }"
        self.assertTrue(TestParser.checkParser(input,expect,300))



    def test_for_statement_1(self):
        input = """
                void main(){
                    int i;
                    for(i = 3; i < infinity; i = i + 1)
                        do
                            statement1;
                            statement2;
                            statement3;
                        while(somethingThatIsTrue);
                    int endline;
                    string[] line;
                }
                """
        expect = "Error on line 11 col 26: ["
        self.assertTrue(TestParser.checkParser(input,expect,242))
    def test_for_statement_2(self):
        input = """
                void main(){
                    int i;
                    for(;;)
                        feelingEmpty = true;
                    int endline;
                    string line;
                }
                """
        expect = "Error on line 4 col 24: ;"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    def test_for_statement_3(self):
        input = """
                void main(){
                    int i;
                    for(i = 3; i < infinity; i = i + 1){
                        for(something; something; something){
                            {//do nothing
                        }}
                    }
                    break;
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    def test_for_statement_4(self):
        input = """
                void main(){
                    int i;
                    for(i = 3; i < infinity; i = i + 1)
                        if(shitHappens)
                            whoCares();
                    for(exp; exp; exp){
                        {
                            stillWhoCares();
                        }
                    }
                    {
                        nowThisIsFun();
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    def test_for_statement_5(self):
        input = """
                void main(){
                    int i;
                    for(i = 3; i < infinity; i = i + 1)
                        continue;
                        return (Continue + Break);
                    break;
                    for(something; something; something)
                        do{}
                        while(something)
                }
                """
        expect = "Error on line 11 col 16: }"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    def test_for_statement_6(self):
        input = """
                void main(){
                    for(;something;something)
                        if(thatMakesYouHappy){}
                        else{
                            print("dontDoThat");
                        }
                    for(something;something;something){
                        int a = 3;
                        a = a * 3 + 4;
                    }
                }
                """
        expect = "Error on line 3 col 24: ;"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    def test_for_statement_7(self):
        input = """
                void main(){
                    int i,j;
                    i = j = 0;
                    for( i = 0; i <= j; i = i + 1){
                        {
                            {
                                // do nothing
                            }
                            var = arr[3];
                        }
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    def test_for_statement_8(self):
        input = """
                void main(){
                    for(life = sea; you = fish; living = swimming){
                        if(fish(sea) != swimming)
                            sea = false;
                        else
                            swimming = swimming + 1;
                        else
                            sea = false;
                    }
                }
                """
        expect = "Error on line 8 col 24: else"
        self.assertTrue(TestParser.checkParser(input,expect,249))



    def test_other_statement_1(self):
        input = """
                void main(){
                    int i;
                    if(willIBeBetter)
                        returnn nothing;
                    break;
                }
                """
        expect = "Error on line 5 col 32: nothing"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    def test_other_statement_2(self):
        input = """
                void main(){
                    funcall(a, a + 1);
                    if(PPL)
                        return "Runnnnnnnnnn";
                    else
                        return;
                    return "Still runnnnnnn";
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    def test_other_statement_3(self):
        input = """
                void main(){
                    do
                        do
                            do
                                continue doingSomething;
                            while("...Yeah no need to check here...");
                }
                """
        expect = "Error on line 6 col 41: doingSomething"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    def test_other_statement_4(self):
        input = """
                void main(){
                    for(test; all; statements)
                        if(thisTestcase == true)
                            do
                                "Yeah you nailed the statements";
                                break;
                                return true;
                                continue;
                            while(stillRunning());
                    printf("Congrats!");
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    def test_other_statement_5(self):
        input = """
                void main(){
                    "So this is nearly the last testcase of this section!";
                    for(test; all; statements)
                        for(test; all_again; statements)
                            if(thisTestcase == true)
                            do
                                "Yeah you nailed the statements";
                                break;
                                return true;
                                continue;
                                do
                                    statement1;
                                    statement2;
                                    statement3;
                                while(stillRunning);
                            while(stillRunning());
                            else{
                                if(yeahHopeYouPassedThis[3000]){
                                    do
                                        maybeThisIsEnough;
                                    while(goodLuck);
                                }
                            }

                    printf("Congrats!");
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    def test_other_statement_6(self):
        input = """
                void main(){
                    "So this is the last testcase of this section! Good luck!";
                    for(test; all; statements)
                        for(test; all_again; statements)
                            if(thisTestcase == true)
                            do
                                "Yeah you nailed the statements";
                                break;
                                return true;
                                continue;
                                do
                                    statement1;
                                    if(youCanPassedThis)
                                        yourStatement = good;
                                    else
                                        needToCheck();
                                while(stillRunning);
                            while(stillRunning());
                            else{
                                if(yeahHopeYouPassedThis[3000]){
                                    do
                                        do
                                            do
                                                for(1;2;3){
                                                    what = doesnot;
                                                    kill = you;
                                                    makes = youStronger;
                                                }
                                                passed = stronger;
                                            while(thisIsGoingToEnd);
                                        while(butThereAreStillManyToCome());
                                    while(goodLuck);
                                }
                            }

                    printf("Congrats!");
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
#===============================================================================================





#========================================TEST EXPRESSIONS========================================
    def test_expression_1(self):
        input = """
                void main(){
                    a = foo(a) + c -2*a;
                    array[3] = foo(array[2] *3) + 34;
                    for(a/b; b%c; c||d)
                        foo(a+b, a-b, arr[3000]);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    def test_expression_2(self):
        input = """
                void main(){
                    if(a < b && b >= c && c > d)
                        doThis();
                    else
                        doThat();
                    exp = a < b > c ;
                }
                """
        expect = "Error on line 7 col 32: >"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    def test_expression_3(self):
        input = """
                void main(){
                    for(a < b + c; a >= b; c[3] + 5){
                        a = b != c == d;
                    }    
                    do
                        makeThis(a*b*c*d/d%e);
                        makeThat(arr[arr[arr[3]]]);
                    while(true);
                }
                """
        expect = "Error on line 4 col 35: =="
        self.assertTrue(TestParser.checkParser(input,expect,258))
    def test_expression_4(self):
        input = """
                void main(){
                    for(-3; -arr[4]; !(arr[3] + b)){
                        a = b = c + d;
                        a != (arr[3] + foo(4));
                    }
                    b = arr && arr = (arr[4] + foo())[3];
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    def test_expression_5(self):
        input = """
                void main(){
                    funcall(a, a + 1);
                    a = funcall(funcall(a[funcall(a[funcall()])]));
                    !a = (ABC + AB[5)*3;
                    return 0;
                }
                int main;
                """
        expect = "Error on line 5 col 36: )"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    def test_expression_6(self):
        input = """
                void main(){
                    {/*
                        This happens inside the scope!
                    }*/
                    if(ABC[ABC[5]]){
                        thereIsSomethingWrong(3lookup);
                    }
                }
                """
        expect = "Error on line 7 col 47: lookup"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    def test_expression_7(self):
        input = """
                void main(){
                    {/*
                        This happens inside the scope!
                    }*/
                    if(ABC[ABC[5]]){
                        thereIsSomethingWrong(lookup);
                    }
                }
                """
        expect = "Error on line 10 col 16: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    def test_expression_8(self):
        input = """
                void main(){
                    if(a3 == 3 + 2[34]){
                        a = A <= b && B <= C < D;
                        main = -!main;
                    }
                }
                """
        expect = "Error on line 4 col 45: <"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    def test_expression_9(self):
        input = """
                void main(){
                    for(foo(a[3]); !fap(a+b,a*b[3+2*6[3]]); i = i + 3.3e-12)
                        do
                            A = A(((((3)))));
                            B = (3.e-2+0.e3)[(4.5+2)[abc]];
                        while(A || B && C || D && E == F);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    def test_expression_10(self):
        input = """
                void main(){
                    int fun(int a, int c){
                        printf("Guess where's the error?")
                        printf("Where is the semicolon?")
                        printf("This is not a function")
                    }
                    int var, var, var[2000];
                }
                """
        expect = "Error on line 3 col 27: ("
        self.assertTrue(TestParser.checkParser(input,expect,265))
    def test_expression_11(self):
        input = """
                string[] createString(int b){
                    for(i = 0; i <= length; i = i + 1){
                        array[i] = (char)*b;
                    }
                }
                void main(){
                    makeThisInt(3)[a+"3.2"];
                    do
                        job1;
                        job2();
                        job3(a[a[a[a[a[job(4)]]]]]);
                    while(working);
                    for(job(); job(); job(job())){
                        if(isJobDone == true)
                            printf("Partyyyy");
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    def test_expression_12(self):
        input = """
                void main(){
                    monitor = "This is some real shit!";
                    A = B * C = C % D / 3.2e-2 && arr[arr(3.4)] || ABC && -3.5 = !true;
                    do{
                        A = B= C = D = E;
                    }{
                        _+_+_+_+_+_+_+_+_+_+_+_+_+_+_;
                    }{
                        _-_-_-_-_-_-_-_-_-_-_-_-_-_;
                    }
                    while(beCrazy());
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    def test_expression_13(self):
        input = """
                void main(){
                    int var;
                    fun(var);
                    float str;
                    fun(fun(str));
                    string a3;
                    fun(fun(fun(a3)));
                    int a[1][1];
                }
                """
        expect = "Error on line 9 col 28: ["
        self.assertTrue(TestParser.checkParser(input,expect,268))
    def test_expression_14(self):
        input = """
                void main(){
                    funcall(a, a + 1);
                    if(youMeetSomeone)
                        return say("Hi");
                    else
                        return A+B*C(a[a[3]]);
                    return "Still runnnnnnn";
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    def test_expression_15(self):
        input = """
                void main(){
                    for(A != B; B = C = D = -E; i+_+){
                        for(A%b; C%D; C[D%E]){
                            createString(createString(createString(a[a[a[4]]])));
                        }
                    }
                }
                """
        expect = "Error on line 3 col 52: )"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    def test_expression_16(self):
        input = """
                void main(int number){
                    int countNumberOfDigit;
                    while(number != 0){
                        countNumberOfDigits++;
                        number = number / 10;
                    }
                    return countNUmberOfDigits;
                }
                """
        expect = "Error on line 4 col 20: while"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    def test_expression_17(self):
        input = """
                void main(){
                    testSomeMassiveThings(true);
                    arr[0] = -arr((arr[1] + arr[2])*(arr[3] * arr[4] / arr[5]))[arr[6]=arr[7]=arr[8] > arr[9]] <= arr[10];
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    def test_expression_18(self):
        input = """
                void main(){
                    funcall(a, a + 1);
                    do
                        do
                            do
                                A = nonAss(a[ass])[ass][ass];
                                B != C = D + E == 6.e-12;
                }
                """
        expect = "Error on line 7 col 55: ["
        self.assertTrue(TestParser.checkParser(input,expect,273))
    def test_expression_19(self):
        input = """
                void main(){
                    funcall(a, a + 1);
                    if(char*b+arr[char*char(b)])
                        for(smt;smt;smt){}
                    else
                        return;
                    arr[arr[arr[]]];
                }
                """
        expect = "Error on line 8 col 32: ]"
        self.assertTrue(TestParser.checkParser(input,expect,274))
    def test_expression_20(self):
        input = """
                void main(){
                    funcall(a, a + 1);
                    do
                        do
                            do
                                A = (nonAss(a[ass])[ass])[ass];
                                B != C = D + E == 6.e-12;
                                While(true);
                            while(true);
                        while(true);
                    While(true);
                    return exit(0);
                }
                """
        expect = "Error on line 14 col 16: }"
        self.assertTrue(TestParser.checkParser(input,expect,275))
#================================================================================================




# ========================================TEST OVERALLS========================================
    def test_overall_1(self):
        input = """
                int isInterrupt;
                int countNumber;
                countNumber = 0;
                void ISR(int isInterrupt){
                    interruptEnable(true);
                    interruptSet(10);
                    interrupt();
                }
                int main(){
                    int count;
                    count = 0;
                    do{
                        checkInterrupt();
                        if(countNumber % 3 == 0) return interruptVector[countNumber];
                        else
                            for(count; count+count; isInterrupt)
                                countNumber = checkInterrupt(interruptVector[countNumber[count]]);
                        noInterrupt();
                    }
                    while(true);
                }
                """
        expect = "Error on line 4 col 16: countNumber"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    def test_overall_2(self):
        input = """
                int isInterrupt;
                int countNumber;
                void ISR(int isInterrupt){
                    interruptEnable(true);
                    interruptSet(10);
                    interrupt();
                }
                int main(){
                    int count;
                    count = 0;
                    countNumber = 0;
                    do{
                        checkInterrupt();
                        if(countNumber % 3 == 0) return interruptVector[countNumber];
                        else
                            for(count; count+count; isInterrupt)
                                countNumber = checkInterrupt(interruptVector[countNumber[count]]);
                        noInterrupt();
                    }
                    while(true);
                }    
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))
    def test_overall_3(self):
        input = """
                int timer0, timer1;
                int threshhold;
                boolean[] checkTimers(){
                    if(timer0 == threshhold)
                        if(timer1 == threshhold)
                            for(i = 0; timer0 == threshhold; i = i + getCycle())
                                do
                                    timer0 = timer1[getCycle * cycle] + checkTimers(timer[timer[timer[checkTimers()]]]);
                                    timer1 = getCycle(cycle1 && cycle2 - 3 * cycle3 != 0);
                                while(timer0 != 0);
                        else
                            checkTimers();
                        timer1 = 0;
                        timer0 = timer1 && checkTimers(checkTimers(timer0[timer1[timer0]]));
                    else
                        return 0;
                }
                """
        expect = "Error on line 16 col 20: else"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    def test_overall_4(self):
        input = """
                int timer0, timer1;
                int threshhold;
                boolean[] checkTimers(){
                    if(timer0 == threshhold)
                        if(timer1 == threshhold)
                            for(i = 0; timer0 == threshhold; i = i + getCycle())
                                do
                                    timer0 = timer1[getCycle * cycle] + checkTimers(timer[timer[timer[checkTimers()]]]);
                                    timer1 = getCycle(cycle1 && cycle2 - 3 * cycle3 != 0);
                                while(timer0 != 0);
                        else
                            checkTimers();
                    timer1 = 0;
                    timer0 = timer1 && checkTimers(checkTimers(timer0[timer1[timer0]]));
                    return 0;
                }        
                int main(){
                    // doing nothing
                };
                """
        expect = "Error on line 20 col 17: ;"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    def test_overall_5(self):
        input = """
                int timer0, timer1;
                int threshhold;
                boolean[] checkTimers(){
                    if(timer0 == threshhold)
                        if(timer1 == threshhold)
                            for(i = 0; timer0 == threshhold; i = i + getCycle())
                                do
                                    timer0 = timer1[getCycle * cycle] + checkTimers(timer[timer[timer[checkTimers()]]]);
                                    timer1 = getCycle(cycle1 && cycle2 - 3 * cycle3 != 0);
                                while(timer0 != 0);
                        else
                            checkTimers();
                    timer1 = 0;
                    timer0 = timer1 && checkTimers(checkTimers(timer0[timer1[timer0]]));                        return 0;
                }
                int main(){
                    int main;
                    break;
                    continue;
                    for(-timer; !timer; timer()){
                        for(i; j; k){
                            if(timer1 !=- timer2 = timer)
                                DO(something);
                        }
                        do
                            for(i; j; k){
                                if(timer1 !=- timer2 == timer)
                                    DO(something);
                            do 
                                makeFile(makeFile[makeFile()]);
                            while(true);
                            }
                        while(true);
                    }
                }
                """
        expect = "Error on line 28 col 53: =="
        self.assertTrue(TestParser.checkParser(input,expect,280))
    def test_overall_6(self):
        input = """
                int timer0, timer1;
                int threshhold;
                boolean[] checkTimers(){
                    if(timer0 == threshhold)
                        if(timer1 == threshhold)
                            for(i = 0; timer0 == threshhold; i = i + getCycle())
                                do
                                    timer0 = timer1[getCycle * cycle] + checkTimers(timer[timer[timer[checkTimers()]]]);
                                    timer1 = getCycle(cycle1 && cycle2 - 3 * cycle3 != 0);
                                while(timer0 != 0);
                        else
                            checkTimers();
                    timer1 = 0;
                    timer0 = timer1 && checkTimers(checkTimers(timer0[timer1[timer0]]));                        return 0;
                }
                int main(){
                    int main;
                    break;
                    continue;
                    for(-timer; !timer; timer()){
                        for(i; j; k){
                            if(timer1 !=- timer2 = timer)
                                DO(something);
                        }
                        do
                            for(i; j; k){
                                if(timer1 !=- timer2 = timer)
                                    DO(something);
                            do 
                                makeFile(makeFile[makeFile()]);
                                !timer1 && timer0 || timer1 = timer0 = timer1 = timer[timer[timer1 + _[timer0[timer0]]]];
                            while(true);
                            }
                        while(true);
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    def test_overall_7(self):
        input = """
                int matrix1, matrix2;
                int sum;
                string[] mul(int matrix1, int matrix2){
                    countMatric = 0;
                    for(i = 0; i < length(sum(matrix1,matrix2)); i = i * countMatrix){
                        countMatrix == matrix1[matrix2[matrix1(countMatrix)]];
                        matrix1 = matrix1 + matrix2 * matrix2(matrix3 * matrix4[matrix(-matrix % matrix5)]);
                        if(matrix1 + matrix2(matrix2(matrix2(countMatrix)))[matrix1+matrix2+countNumber]){
                            return true;
                            break;
                            continue;
                        }
                        else{
                            crateMatrix(matrix1, matrix2, sumMatrix(matrix1, matrix2));
                            do{
                                if(matrix1 * matrix2[matrix2-matrix3[countNumber[_[_[3]]]]){
                                    replace(matrix1) = !matrix2 - matrix4 * -matrix5;
                                }
                                do
                                    for(matrix1[matrix2 - matrix3(matrix1)]; matrix1(matrix1(matrix1[matrix2()]); !matrix1 - matrix2*(matrix1 - matrix2*(matrix1 * matrix2))){
                                        matrix1 = - matrix2;
                                    }
                                while(matrix1 != -matrix2);
                            }
                            while(matrix1 == matrix2);
                        }
                    }
                };
                """
        expect = "Error on line 17 col 90: )"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    def test_overall_8(self):
        input = """
                int matrix1, matrix2;
                int sum;
                string[] mul(int matrix1, int matrix2){
                    countMatric = 0;
                    for(i = 0; i < length(sum(matrix1,matrix2)); i = i * countMatrix){
                        countMatrix == matrix1[matrix2[matrix1(countMatrix)]];
                        matrix1 = matrix1 + matrix2 * matrix2(matrix3 * matrix4[matrix(-matrix % matrix5)]);
                        if(matrix1 + matrix2(matrix2(matrix2(countMatrix)))[matrix1+matrix2+countNumber]){
                            return true;
                            break;
                            continue;
                        }
                        else{
                            crateMatrix(matrix1, matrix2, sumMatrix(matrix1, matrix2));
                            do{
                                if(matrix1 * matrix2[matrix2-matrix3[countNumber[_[_[3]]]]]){
                                    replace(matrix1) = !matrix2 - matrix4 * -matrix5;
                                }
                                do
                                    for(matrix1[matrix2 - matrix3(matrix1)]; matrix1(matrix1(matrix1[matrix2()]); !matrix1 - matrix2*(matrix1 - matrix2*(matrix1 * matrix2))){
                                        matrix1 = - matrix2;
                                    }
                                while(matrix1 != -matrix2);
                            }
                            while(matrix1 == matrix2);
                        }
                    }
                }
                """
        expect = "Error on line 21 col 112: ;"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    def test_overall_9(self):
        input = """
                int matrix1, matrix2;
                int sum;
                string[] mul(int matrix1, int matrix2){
                    countMatric = 0;
                    for(i = 0; i < length(sum(matrix1,matrix2)); i = i * countMatrix){
                        countMatrix == matrix1[matrix2[matrix1(countMatrix)]];
                        matrix1 = matrix1 + matrix2 * matrix2(matrix3 * matrix4[matrix(-matrix % matrix5)]);
                        if(matrix1 + matrix2(matrix2(matrix2(countMatrix)))[matrix1+matrix2+countNumber]){
                            return true;
                            break;
                            continue;
                        }
                        else{
                            crateMatrix(matrix1, matrix2, sumMatrix(matrix1, matrix2));
                            do{
                                if(matrix1 * matrix2[matrix2-matrix3[countNumber[_[_[3]]]]]){
                                    replace(matrix1) = !matrix2 - matrix4 * -matrix5;
                                }
                                do
                                    for(matrix1[matrix2 - matrix3(matrix1)]; matrix1(matrix1(matrix1[matrix2()])); !matrix1 - matrix2*(matrix1 - matrix2*(matrix1 * matrix2))){
                                        matrix1 = - matrix2;
                                    }
                                while(matrix1 != -matrix2);
                            }
                            while(matrix1 == matrix2);
                        }
                    }
                }
                int main(){
                    int count;
                    float set;
                    string matrix;
                    for(matrix1[matrix2[matrix2()]]; matrix1 * ( matrix1 * matrix2(matrix1 * matrix2)); matrix1(matrix1(matrix1 + matrix2 && matrix1 - matrix2 || matrix2))){
                        for(matrix1*matrix2*matrix3*matrix4; matrix1+matrix2+matrix3+matrix4; -matrix1-matrix2-matrix3-matrix4){
                            do
                                createMatrix(matrix1%matrix2%matrix, matrix1 < matrix3 || matrix2 >= matrix4);
                                if(matrix1 <= -matrix2 + matrix2[matrix3()]){
                                    matrix2 = matrix3 * matrix3[matrix2[matrix3,]];
                                }
                                else{
                                    createMatrix(matrix1&&matrix2,matrix1||matrix3,matrix4());
                                }
                            while(true);
                        }
                    }
                } 
                """
        expect = "Error on line 39 col 79: ,"
        self.assertTrue(TestParser.checkParser(input,expect,284))
    def test_overall_10(self):
        input = """
                int matrix1, matrix2;
                int sum;
                string[] mul(int matrix1, int matrix2){
                    countMatric = 0;
                    for(i = 0; i < length(sum(matrix1,matrix2)); i = i * countMatrix){
                        countMatrix == matrix1[matrix2[matrix1(countMatrix)]];
                        matrix1 = matrix1 + matrix2 * matrix2(matrix3 * matrix4[matrix(-matrix % matrix5)]);
                        if(matrix1 + matrix2(matrix2(matrix2(countMatrix)))[matrix1+matrix2+countNumber]){
                            return true;
                            break;
                            continue;
                        }
                        else{
                            crateMatrix(matrix1, matrix2, sumMatrix(matrix1, matrix2));
                            do{
                                if(matrix1 * matrix2[matrix2-matrix3[countNumber[_[_[3]]]]]){
                                    replace(matrix1) = !matrix2 - matrix4 * -matrix5;
                                }
                                do
                                    for(matrix1[matrix2 - matrix3(matrix1)]; matrix1(matrix1(matrix1[matrix2()])); !matrix1 - matrix2*(matrix1 - matrix2*(matrix1 * matrix2))){
                                        matrix1 = - matrix2;
                                    }
                                while(matrix1 != -matrix2);
                            }
                            while(matrix1 == matrix2);
                        }
                    }
                }
                int main(){
                    int count;
                    float set;
                    string matrix;
                    for(matrix1[matrix2[matrix2()]]; matrix1 * ( matrix1 * matrix2(matrix1 * matrix2)); matrix1(matrix1(matrix1 + matrix2 && matrix1 - matrix2 || matrix2))){
                        for(matrix1*matrix2*matrix3*matrix4; matrix1+matrix2+matrix3+matrix4; -matrix1-matrix2-matrix3-matrix4){
                            do
                                createMatrix(matrix1%matrix2%matrix, matrix1 < matrix3 || matrix2 >= matrix4);
                                if(matrix1 <= -matrix2 + matrix2[matrix3()]){
                                    matrix2 = matrix3 * matrix3[matrix2[matrix3]];
                                }
                                else{
                                    createMatrix(matrix1&&matrix2,matrix1||matrix3,matrix4());
                                    do
                                        create(create(create(create())));
                                        for(matrix1*matrix2/matrix3+4; matrix1 || matrix2 && matrix1 * matrix2; !matrix1){
                                            return true;
                                            break;
                                            continue;
                                        }
                                    while(!matrix1 == matrix2 = matrix1 == matrix2 == matrix1);
                                }
                            while(true);
                        }
                    }
                }
                """
        expect = "Error on line 50 col 83: =="
        self.assertTrue(TestParser.checkParser(input,expect,300))
    def test_overall_11(self):
        input = """
                int matrix1, matrix2;
                int sum;
                string[] mul(int matrix1, int matrix2){
                    countMatric = 0;
                    for(i = 0; i < length(sum(matrix1,matrix2)); i = i * countMatrix){
                        countMatrix == matrix1[matrix2[matrix1(countMatrix)]];
                        matrix1 = matrix1 + matrix2 * matrix2(matrix3 * matrix4[matrix(-matrix % matrix5)]);
                        if(matrix1 + matrix2(matrix2(matrix2(countMatrix)))[matrix1+matrix2+countNumber]){
                            return true;
                            break;
                            continue;
                        }
                        else{
                            crateMatrix(matrix1, matrix2, sumMatrix(matrix1, matrix2));
                            do{
                                if(matrix1 * matrix2[matrix2-matrix3[countNumber[_[_[3]]]]]){
                                    replace(matrix1) = !matrix2 - matrix4 * -matrix5;
                                }
                                do
                                    for(matrix1[matrix2 - matrix3(matrix1)]; matrix1(matrix1(matrix1[matrix2()])); !matrix1 - matrix2*(matrix1 - matrix2*(matrix1 * matrix2))){
                                        matrix1 = - matrix2;
                                    }
                                while(matrix1 != -matrix2);
                            }
                            while(matrix1 == matrix2);
                        }
                    }
                }
                int main(){
                    int count;
                    float set;
                    string matrix;
                    for(matrix1[matrix2[matrix2()]]; matrix1 * ( matrix1 * matrix2(matrix1 * matrix2)); matrix1(matrix1(matrix1 + matrix2 && matrix1 - matrix2 || matrix2))){
                        for(matrix1*matrix2*matrix3*matrix4; matrix1+matrix2+matrix3+matrix4; -matrix1-matrix2-matrix3-matrix4){
                            do
                                createMatrix(matrix1%matrix2%matrix, matrix1 < matrix3 || matrix2 >= matrix4);
                                if(matrix1 <= -matrix2 + matrix2[matrix3()]){
                                    matrix2 = matrix3 * matrix3[matrix2[matrix3]];
                                }
                                else{
                                    createMatrix(matrix1&&matrix2,matrix1||matrix3,matrix4());
                                    do
                                        create(create(create(create())));
                                        for(matrix1*matrix2/matrix3+4; matrix1 || matrix2 && matrix1 * matrix2; !matrix1){
                                            return true;
                                            break;
                                            continue;
                                        }
                                    while(!matrix1 == matrix2 = matrix1 == matrix2 = matrix1 != matrix1 = -matrix2);
                                }
                            while(true);
                        }
                    }
                } 
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    def test_overall_12(self):
        input = """
                int matrix1, matrix2;
                int sum;
                string[] mul(int matrix1, int matrix2){
                    countMatric = 0;
                    for(i = 0; i < length(sum(matrix1,matrix2)); i = i * countMatrix){
                        countMatrix == matrix1[matrix2[matrix1(countMatrix)]];
                        matrix1 = matrix1 + matrix2 * matrix2(matrix3 * matrix4[matrix(-matrix % matrix5)]);
                        if(matrix1 + matrix2(matrix2(matrix2(countMatrix)))[matrix1+matrix2+countNumber]){
                            return true;
                            break;
                            continue;
                        }
                        else{
                            crateMatrix(matrix1, matrix2, sumMatrix(matrix1, matrix2));
                            do{
                                if(matrix1 * matrix2[matrix2-matrix3[countNumber[_[_[3]]]]]){
                                    replace(matrix1) = !matrix2 - matrix4 * -matrix5;
                                }
                                do
                                    for(matrix1[matrix2 - matrix3(matrix1)]; matrix1(matrix1(matrix1[matrix2()])); !matrix1 - matrix2*(matrix1 - matrix2*(matrix1 * matrix2))){
                                        matrix1 = - matrix2;
                                    }
                                while(matrix1 != -matrix2);
                            }
                            while(matrix1 == matrix2);
                        }
                    }
                }
                int main(){
                    int count;
                    float set;
                    string matrix;
                    for(matrix1[matrix2[matrix2()]]; matrix1 * ( matrix1 * matrix2(matrix1 * matrix2)); matrix1(matrix1(matrix1 + matrix2 && matrix1 - matrix2 || matrix2))){
                        for(matrix1*matrix2*matrix3*matrix4; matrix1+matrix2+matrix3+matrix4; -matrix1-matrix2-matrix3-matrix4){
                            do
                                createMatrix(matrix1%matrix2%matrix, matrix1 < matrix3 || matrix2 >= matrix4);
                                if(matrix1 <= -matrix2 + matrix2[matrix3()]){
                                    matrix2 = matrix3 * matrix3[matrix2[matrix3]];
                                }
                                else{
                                    createMatrix(matrix1&&matrix2,matrix1||matrix3,matrix4());
                                    do
                                        create(create(create(create())));
                                        for(matrix1*matrix2/matrix3+4; matrix1 || matrix2 && matrix1 * matrix2; !matrix1){
                                            return true;
                                            break;
                                            continue;
                                        }
                                    while(!matrix1 == matrix2 = matrix1 == matrix2 = matrix1 != matrix1 = -matrix2);
                                    if(matrix1==matrix2 = matrix3 - matrix3 % 34.e-12){}
                                }
                            while(true);
                        }
                    }
                }
                int fl0at;
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    def test_overall_13(self):
        input = """
                int return_to_easy_testases;
                float[] function(int a, string b, boolean c){
                    for(i = 0; i <= 9; i = i * 3){
                        if(arr[i] == 3) return true;
                        else continue;
                        do
                            A = B + C * D % E == F && G;
                            return B != -C+D*EF[EF[EF()]];
                            int a;
                        while(A == B = C);
                    }
                    float string;
                }
                """
        expect = "Error on line 10 col 28: int"
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test_overall_14(self):
        input = """
                int a;
                float b;
                
                float[] function(int a, string b, boolean c){
                    if(a == b && b != c[c*c[3*4]]){
                        createString(a,b,c[3.4e-112]);
                        do
                            youAlmostThere = 1;
                            name = "Phan Gia Anh";
                        while(true);
                        for(fun; sad; tear){
                            A = B = C = D = E % F % G && H && I && J;
                        }
                    }
                } 
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    def test_overall_15(self):
        input = """
                int a;
                string b;
                boolean c;

                boolean[] create(){
                    int main;
                    float main;
                    string main;
                    for(smt1; smt2; smt3){
                        smt1((((((((smt2))))))));
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))
    def test_overall_16(self):
        input = """
                // Here are heavy-workload testcases
                int a[99999999];
                float b[00000000000000000000000];
                int[] main(){
                    for(a[a[a[a[a[45]]]]]; fun((((((3)))))); a[fun(a[fun(a[fun()])])]){
                        for(a*(a*(a*(a*(3)))); a-(a-(a-(a-(4)))); a+(a+(a+(a+(a+(5)))))){
                            if(a/3/4/5/6/7/8){
                                //save for other testcases :)))
                            }
                            else{
                                do
                                    // doing nothing here
                                    do
                                        do
                                            // still doing nothing here
                                        while(true);
                                    while(true);
                                while(true);
                            }
                        }
                        if(A=(B=(C=(D=(a))))){
                            for(something; something; something){
                                for(something; something; something){
                                    */ doing nothing here */
                                }
                            }
                        }
                    }
                }
                """
        expect = "Error on line 17 col 40: while"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    def test_overall_17(self):
        input = """
                int a[99999999];
                float b[00000000000000000000000];
                string c[666666666666666];
                int[] main(){
                    for(a[a[a[a[a[45]]]]]; fun((((((3)))))); a[fun(a[fun(a[fun()])])]){
                        for(a*(a*(a*(a*(3)))); a-(a-(a-(a-(4)))); a+(a+(a+(a+(a+(5)))))){
                            if(a/3/4/5/6/7/8){
                                createString(a*b[b[b[b[b[3]]]]]-a(a(a(a(3)))));
                                for( i = a[i=a[i=a[i=a[3]]]]; i >= 0 && b - c * a[2]; i = i + a[i+a[i+a[i+a[3]]]]){
                                    do
                                        do
                                            for(a[a[a[3]]]; foo(foo(foo(3))); a[foo(a[foo()])]) printf("Hope you passed this");
                                        while(a == b = c = d = e);
                                    while(a+a+a+a+a+a+a+a+a+a+a+a);
                                }
                            }
                            else{
                                do
                                    // doing nothing here
                                    do
                                        do{}
                                            // still doing nothing here
                                        while(true);
                                    while(true);
                                while(true);
                            }
                        }
                        if(A=(B=(C=(D=(a))))){
                            for(something; something; something){
                                for(something; something; something){
                                    /* doing nothing here */
                                }
                            }
                        }
                    }
                } 
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    def test_overall_18(self):
        input = """
                int a[99999999];
                float b[00000000000000000000000];
                string c[666666666666666];
                int[] main(){
                    for(a[a[a[a[a[45]]]]]; fun((((((3)))))); a[fun(a[fun(a[fun()])])]){
                        for(a*(a*(a*(a*(3)))); a-(a-(a-(a-(4)))); a+(a+(a+(a+(a+(5)))))){
                            if(a/3/4/5/6/7/8){
                                createString(a*b[b[b[b[b[3]]]]]-a(a(a(a(3)))));
                                for( i = a[i=a[i=a[i=a[3]]]]; i >= 0 && b - c * a[2]; i = i + a[i+a[i+a[i+a[3]]]]){
                                    do
                                        do
                                            for(a[a[a[3]]]; foo(foo(foo(3))); a[foo(a[foo()])]) printf("Hope you passed this");
                                        while(a == b = c = d = e);
                                    while(a+a+a+a+a+a+a+a+a+a+a+a);
                                }
                            }
                            else{
                                do
                                    for(a(((((a))))); b(((((b))))); c[c[c[c[c[c[c]]]]]]){
                                        do
                                            if(condition == true || false || notTrueOrFalse && condition[true]){
                                                //doing something here
                                            }
                                            do
                                                makeThis(makeThis(makeThis()));
                                                makeThat[makeThat[makeThat[expression]]];
                                                do
                                                    // waiting
                                                while(true);
                                            while(true);
                                    }
                                    do
                                        do{}
                                            // still doing nothing here
                                        while(true);
                                    while(true);
                                while(true);
                            }
                        }
                        if(A=(B=(C=(D=(a))))){
                            for(something; something; something){
                                for(something; something; something){
                                    /* doing nothing here */
                                }
                            }
                        }
                    }
                }  
                """
        expect = "Error on line 30 col 48: while"
        self.assertTrue(TestParser.checkParser(input,expect,293))
    def test_overall_19(self):
        input = """
                int a[99999999];
                float b[00000000000000000000000];
                string c[666666666666666];
                int[] main(){
                    for(a[a[a[a[a[45]]]]]; fun((((((3)))))); a[fun(a[fun(a[fun()])])]){
                        for(a*(a*(a*(a*(3)))); a-(a-(a-(a-(4)))); a+(a+(a+(a+(a+(5)))))){
                            if(a/3/4/5/6/7/8){
                                createString(a*b[b[b[b[b[3]]]]]-a(a(a(a(3)))));
                                for( i = a[i=a[i=a[i=a[3]]]]; i >= 0 && b - c * a[2]; i = i + a[i+a[i+a[i+a[3]]]]){
                                    do
                                        do
                                            for(a[a[a[3]]]; foo(foo(foo(3))); a[foo(a[foo()])]) printf("Hope you passed this");
                                        while(a == b = c = d = e);
                                    while(a+a+a+a+a+a+a+a+a+a+a+a);
                                }
                            }
                            else{
                                do
                                    for(a(((((a))))); b(((((b))))); c[c[c[c[c[c[c]]]]]]){
                                        do
                                            if(condition == true || false || notTrueOrFalse && condition[true]){
                                                //doing something here
                                            }
                                            do
                                                makeThis(makeThis(makeThis()));
                                                makeThat[makeThat[makeThat[expression]]];
                                                do
                                                {
                                                    for(i - i[i-i[i-i[i-i[]]]]; something; something){
                                                        return foo(A*A*A*A*A*A*A*A*A*A*A*A);
                                                    }
                                                }
                                                while(true);
                                            while(true);
                                    }
                                    do
                                        do{}
                                            // still doing nothing here
                                        while(true);
                                    while(true);
                                while(true);
                            }
                        }
                        if(A=(B=(C=(D=(a))))){
                            for(something; something; something){
                                for(something; something; something){
                                    /* doing nothing here */
                                }
                            }
                        }
                    }
                } 
                """
        expect = "Error on line 30 col 74: ]"
        self.assertTrue(TestParser.checkParser(input,expect,294))
    def test_overall_20(self):
        input = """
                // Final heavy-workload testcase
                int a[99999999];
                float b[00000000000000000000000];
                string c[666666666666666];
                int[] main(){
                    for(a[a[a[a[a[45]]]]]; fun((((((3)))))); a[fun(a[fun(a[fun()])])]){
                        for(a*(a*(a*(a*(3)))); a-(a-(a-(a-(4)))); a+(a+(a+(a+(a+(5)))))){
                            if(a/3/4/5/6/7/8){
                                createString(a*b[b[b[b[b[3]]]]]-a(a(a(a(3)))));
                                for( i = a[i=a[i=a[i=a[3]]]]; i >= 0 && b - c * a[2]; i = i + a[i+a[i+a[i+a[3]]]]){
                                    do
                                        do
                                            for(a[a[a[3]]]; foo(foo(foo(3))); a[foo(a[foo()])]) printf("Hope you passed this");
                                        while(a == b = c = d = e);
                                    while(a+a+a+a+a+a+a+a+a+a+a+a);
                                }
                            }
                            else{
                                do
                                    for(a(((((a))))); b(((((b))))); c[c[c[c[c[c[c]]]]]]){
                                        do
                                            if(condition == true || false || notTrueOrFalse && condition[true]){
                                                createWorld("Hello World" + "HelloW World"["Hello World" + _[_[_[_]]]]);
                                            }
                                            do
                                                makeThis(makeThis(makeThis()));
                                                makeThat[makeThat[makeThat[expression]]];
                                                do
                                                {
                                                    for(i - i[i-i[i-i[i-i[3]]]]; something; something){
                                                        return foo(A*A*A*A*A*A*A*A*A*A*A*A);
                                                    }
                                                }
                                                while(true);
                                            while(true);
                                        while(true);
                                    }
                                    do
                                        do{
                                            for(something; something; something){
                                                if(thisIsTrue)
                                                    printf("Well done");
                                                else
                                                    printf("Try again");
                                            }
                                        }
                                        while(true);
                                    while(true);
                                while(true);
                            }
                        }
                        if(A=(B=(C=(D=(a))))){
                            for(something; something; something){
                                for(something; something; something){
                                    if(youCanMakeThis){
                                        printf("Congratulations!");
                                        printf("Well done!");
                                    }
                                }
                            }
                        }
                    }
                }        
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))
    def test_overall_21(self):
        input = """
                int main(){
                    for(something; something; something){
                        printf("This is the end of these testcases");
                    }
                    if(passed){
                        printf("You should be proud for what you have done!");
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))
    def test_overall_22(self):
        input = """
                int main(){
                    do
                        printf("These last 5 testcases outputs are all successful");
                    while("Hope you will too!");
                    if(difficult){
                        printf("Don't be afraid to count on your friend");
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    def test_overall_23(self):
        input = """
                int[] main(){
                    if(feeling == depression){
                        printf("Believe in the future and move on");
                    }
                    else{
                        actFromNowOn(now);
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))
    def test_overall_24(self):
        input = """
                int main(){
                    do
                        enjoyYourLife(true);
                        makeABetterVersionOfYourSelf(true);
                    while(lifeIsShort());
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    def test_overall_25(self):
        input = """
                int main(){
                    justRemember();
                    printf("Falling is the chance of Flying");
                    goodLuck("PhanGiaAnh");
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))
#=============================================================================================




        

    