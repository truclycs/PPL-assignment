# 1712345
# Dang Minh Ngoc
import unittest
from TestUtils import TestChecker
from AST import *

class CheckSuite(unittest.TestCase):
#------------------------------------------------------------------------------------------------------
    def test_redeclared_var_in_global_scope(self):
        "test_no_entry_point"
        input = """int global, scope[100];
        void main() {
            // Do nothing in here
        }
        float scope;"""
        expect = "Redeclared Variable: scope"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_global_var_in_local_scope(self):
        "test_no_entry_point"
        input = """int global, scope[100];
        void main() {
            int global[10];
            return ;
            // Do nothing in here
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_var_in_local_scope(self):
        input = """int global, scope[100];
        void main() {
            int a,b;
            float x,y,a[10], t;
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_var_with_func_name(self):
        input = """int global, scope[100];
        void main() {
            // Do nothing in here
        }
        float main;"""
        expect = "Redeclared Variable: main"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_var_in_local_scope_with_func_name(self):
        input = """int global, scope[100];
        void main() {
            boolean main[100];
            int bts, yoongi;
            // Do nothing in here
        }
        float arr[10];"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_redeclared_func(self):
        input = """int global, scope[100];
        void main() {
            // Do nothing in here
        }
        int main(float var1, float var_arr[]) {
            var1 = var_arr[0];
            return 1+0-1;
        }"""
        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_redeclared_func_with_local_var_name(self):
        input = """int global;
        
        void main() {
            // Do nothing in here
            scope("Born Coder :>");
            {int scope;}
        }
        float scope(string message) {
            putString(message);
            return getFloat();
        }"""
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redeclared_func_with_var_name(self):
        input = """int global, scope[100];
        void main() {
            // Do nothing in here
        }
        float scope(string message) {
            putString(message);
            return getFloat();
        }"""
        expect = "Redeclared Function: scope"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_redeclared_param(self):
        input = """int global, scope[100];
        int main(int BTS, string BTS[]) {
           int a;
           a = 10;
           return a; 
        }
        """
        expect = "Redeclared Parameter: BTS"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_redeclared_param_with_global_id(self):
        input = """int global, scope[100];
        void main(int global, int main) {
            // Do nothing in here
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_undeclared_id(self):
        input = """int JIN, SUGA;
        void main(int global, int main) {
            {
                SUGA + JIN > SUGA - JIN;
            }
            RM = "leader";
        }
        """
        expect = "Undeclared Identifier: RM"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_undeclared_id2(self):
        input = """string BTS[7];
        void main(int global, int main) {
            global = pow(BTS,7);
        }
        int pow(string idol[], int no){
            putString(idol[7]);
            return no*_well_known;
        }
        """
        expect = "Undeclared Identifier: _well_known"
        self.assertTrue(TestChecker.test(input,expect,411))
    
    def test_undeclared_func(self):
        input = """string FourIV;
        int main(int global, int main) {
            putInt(exp);
            global = pow(FourIV,7);
            return global;
        }
        int exp;

        """
        expect = "Undeclared Function: pow"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_undeclared_func2(self):
        input = """string FourIV;
        int main(int global, int main) {
            putInt(exp);
            global = (getInt()*7);
            return global;
        }
        int exp;
        void factor(int a, int b) {
            a=b=exp;
            print(a+b);
            return ;
        }

        """
        expect = "Undeclared Function: print"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_type_mismatch_stmt_in_if_else(self):
        input = """
        // Global scope here
        string os_greets, str;
        int arr[10];
        int main(int global, int main) {
            putString(os_greets);
            global = exp(arr);
            return global;
        }
        int exp(int array[]){
            //Get value
            int index;
            index = getInt();
            if (index < array[index]) 
                return index;
            else
                return index + array[index];
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_type_mismatch_stmt_in_if(self):
        input = """
        int main(int global, int main) {
            putString("Hello World");
            exp(130613);
            return global;
        }
        void exp(int i){
            //Get value
            int index;
            index = random[0] = getInt();
            if (getFloat()) 
                return ;
        }
        int random[1]; 
        """
        expect = "Type Mismatch In Statement: If(CallExpr(Id(getFloat),[]),Return())"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_type_mismatch_stmt_in_for(self):
        input = """
        int main() {
            int i;
            for (i = 1; i < 11; 1+i)
            {
                putString("%d i");
            }
            return 0;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_type_mismatch_stmt_in_for_expr1(self):
        input = """
        int main() {
            int i;
            i = 10;
            for (getFloat()*1-getInt(); i < 11; 1+i)
            {
                putString("%d i");
            }
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(-,BinaryOp(*,CallExpr(Id(getFloat),[]),IntLiteral(1)),CallExpr(Id(getInt),[]));BinaryOp(<,Id(i),IntLiteral(11));BinaryOp(+,IntLiteral(1),Id(i));Block([CallExpr(Id(putString),[StringLiteral(%d i)])]))"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_type_mismatch_stmt_in_for_expr2(self):
        input = """
        int main() {
            int i;
            for (i = 1; ((i)); 1+i)
            {
                putString("%d i");
            }
            return 0;
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));Id(i);BinaryOp(+,IntLiteral(1),Id(i));Block([CallExpr(Id(putString),[StringLiteral(%d i)])]))"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_type_mismatch_stmt_in_for_expr3(self):
        input = """
        void main() {
            int i;
            for (i = 1; i < 11; "hello world")
            {
                putString("%d i");
            }
        }
        """
        expect = "Type Mismatch In Statement: For(BinaryOp(=,Id(i),IntLiteral(1));BinaryOp(<,Id(i),IntLiteral(11));StringLiteral(hello world);Block([CallExpr(Id(putString),[StringLiteral(%d i)])]))"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_type_mismatch_stmt_in_dowhile(self):
        input = """
        int main()
        {
	        int j;
            j=0;
	        do
	        {
		        printf("Value of variable j is: %d", j);
		        j = j+1;
	        }while (j<=3);
	        return 0;
        }
        void printf(string str, int elem) {
            putString(str);
            putInt(elem);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_type_mismatch_stmt_in_dowhile_cond(self):
        input = """
        int main()
        {
	        int j;
            j=0;
	        do
	        {
		        printf("Value of variable j is: %d", j);
		        j = j+1;
	        }while (printf("Error here", 1));
	        return 0;
        }
        void printf(string str, int elem) {
            putString(str);
            putInt(elem);
        }
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([CallExpr(Id(printf),[StringLiteral(Value of variable j is: %d),Id(j)]),BinaryOp(=,Id(j),BinaryOp(+,Id(j),IntLiteral(1)))])],CallExpr(Id(printf),[StringLiteral(Error here),IntLiteral(1)]))"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_type_mismatch_stmt_return_void(self):
        input = """
        void main(int argc)
        {
	        return printf("greetings from main", 10);
        }
        void printf(string str, int elem) {
            putString(str);
            putInt(elem);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_type_mismatch_stmt_return_nothing(self):
        input = """
        void main(int argc)
        {
            printf("What to do?", argc);
	        return ;
        }
        void printf(string str, int elem) {
            putString(str);
            putInt(elem);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_type_mismatch_stmt_return_matching_case(self):
        input = """
        int main(int argc, string argv[])
        {
            argv[0] = printf("What to do?", argc);
	        return 0;
        }
        string printf(string str, int elem) {
            putString(str);
            putInt(elem);
            return ;
        }
        """
        expect = "Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_type_mismatch_stmt_return_matching_case2(self):
        input = """
        boolean main(int argc, string argv[])
        {
            argv[0] = printf("Executing...", argc);
            if (argc != 0)
	            return true;
            else
                return 0;
        }
        string printf(string str, int elem) {
            putString(str);
            elem = getInt();
            return "completed";
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_type_mismatch_stmt_return_coerced_case(self):
        input = """
        float base;
        boolean main(int argc, float argv[])
        {
            putFloat(greater(argv, argc));
            return true;
        }
        float greater(float arr[], int idx) {
            if (arr[idx] >= base)
                return idx;
            else
                return -1;            
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_type_mismatch_stmt_return_coerced_case2(self):
        input = """
        float base;
        boolean main(int argc, float argv[])
        {
            putInt(greater(argv, argc));
            return true;
        }
        int greater(float arr[], int idx) {
            if (arr[idx] >= base)
                return arr[idx];
            else
                return -1;            
        }
        """
        expect = "Type Mismatch In Statement: Return(ArrayCell(Id(arr),Id(idx)))"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_type_mismatch_stmt_return_array(self):
        input = """
        float base;
        void main(int argc, float argv[])
        {
            greater(argv, argc);
            return ;
        }
        float[] greater(float arr[], int idx) {
            if (arr[idx] >= base)
                return arr;
            else {
                float tmp[10];
                return tmp;  
            }          
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_type_mismatch_stmt_return_array2(self):
        input = """
        float base;
        float[] main(int argc, int argv[])
        {
            
            return greater(argv, argc);
        }
        int[] greater(int arr[], int idx) {
            if (arr[idx] >= base)
                return arr;
            else {
                int tmp[10];
                return tmp;  
            }          
        }
        """
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(greater),[Id(argv),Id(argc)]))"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_type_mismatch_expr_arr_subscript(self):
        input = """
        int yoongi;
        void main(int argc, int argv[])
        {
            BTS(argv, argc)[0] = yoongi;
        }
        int[] BTS(int arr[], int idx) {
            if (arr[idx] >= yoongi)
                return arr;
            else {
                int tmp[10];
                return tmp;  
            }          
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_type_mismatch_expr_arr_subscript(self):
        input = """
        int yoongi;
        void main(int argc, int argv[])
        {
            float error_idx;
            error_idx = 0.0;
            {
                BTS(argv, argc)[error_idx] = yoongi;
            }
        }
        int[] BTS(int arr[], int idx) {
            if (arr[idx] >= yoongi)
                return arr;
            else {
                int tmp[10];
                return tmp;  
            }          
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(BTS),[Id(argv),Id(argc)]),Id(error_idx))"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_type_mismatch_expr_arr_subscript2(self):
        input = """
        int yoongi;
        void main(int argc, int argv[])
        {
            float error_idx;
            error_idx = 0.0;
            {
                BTS(argv, argc)[7] = yoongi;
            }
        }
        int BTS(int arr[], int idx) {
            if (arr[idx] >= yoongi)
                return idx;
            else {
                return -1;  
            }          
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(BTS),[Id(argv),Id(argc)]),IntLiteral(7))"
        self.assertTrue(TestChecker.test(input,expect,431))
    
    def test_type_mismatch_expr_binary_assign(self):
        input = """
        int global;
        void main(int argc, int argv[])
        {
            int x,y,z;
            boolean t;
            x=y=z=global=1;
            t=true;
            {
                string str;
                str = "Minh Ngoc";
                float f;
                f = 1.5e-09;
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_type_mismatch_expr_binary_assign2(self):
        input = """
        int global;
        void main(int argc, int argv[])
        {
            int x,y,z;
            float a;
            a = 1;
            x = a;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(x),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_type_mismatch_expr_binary_assign_lhs_is_func_name(self):
        input = """
        int global;
        string swap(int a, int b) {
            int t;
            t = a;
            a = b; b= t;
            return "Done";
        }
        int main(string argv)
        {
            swap = argv;
            return 0;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(swap),Id(argv))"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_type_mismatch_expr_binary_assign_arr_address_as_operands(self):
        input = """
        int arr[10];
        void main(int argc, int argv[])
        {
            int main[1];
            {
                arr = main;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(=,Id(arr),Id(main))"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_type_mismatch_expr_binary_num_op(self):
        input = """
        int arr[10];
        void main(int argc, int argv[])
        {
            2+5;
            3.5-6e-1;
            2*3.7;
            1/3*7;
            {
                int a,b,c[2];
                float x,y,z[10];
                a = b = 0;
                x = y = .5;
                a*b - 5 +7/5;
                3-a+x*b-c[0];
                z[5] / 4 + 3 * c[1];
            }
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_type_mismatch_expr_binary_add_string(self):
        input = """
        int arr[10];
        void main(int argc, int argv[])
        {
            arr[1] + "string";
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,ArrayCell(Id(arr),IntLiteral(1)),StringLiteral(string))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_type_mismatch_expr_binary_divide_boolean(self):
        input = """
        int arr[10];
        void main(int argc, int argv[])
        {
            boolean b;
            b = false;
            arr[1] + b;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,ArrayCell(Id(arr),IntLiteral(1)),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_type_mismatch_expr_binary_mod_float(self):
        input = """
        int arr[10];
        void main(int argc, int argv[])
        {
            float t;
            t = 0.0;
            arr[1] % (arr[0]/arr[1]*t);
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(%,ArrayCell(Id(arr),IntLiteral(1)),BinaryOp(*,BinaryOp(/,ArrayCell(Id(arr),IntLiteral(0)),ArrayCell(Id(arr),IntLiteral(1))),Id(t)))"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_type_mismatch_expr_binary_logic_op(self):
        input = """
        int arr[10];
        void main(int argc, int argv[])
        {
            boolean b;
            b = false || true && (1==1) || !(2>=4);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_type_mismatch_expr_binary_or_number(self):
        input = """
        int arr[10];
        void main(int argc, int argv[])
        {
            2 || arr[9];
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(||,IntLiteral(2),ArrayCell(Id(arr),IntLiteral(9)))"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_type_mismatch_expr_binary_compare_string(self):
        input = """
        int arr[10];
        void main(int argc, int argv[])
        {
            arr[0] == "string error";
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,ArrayCell(Id(arr),IntLiteral(0)),StringLiteral(string error))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_type_mismatch_expr_binary_and_int(self):
        input = """
        float arr[10];
        void main(int argc, int argv[])
        {
            boolean b;
            b = arr[0] >= 1 || true;
            b && 1;
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,Id(b),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_type_mismatch_expr_unary(self):
        input = """
        float arr[10];
        void main(int argc, int argv[])
        {
            boolean b;
            b = arr[0] >= 1 || true;
            -b;
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(b))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_type_mismatch_expr_unary2(self):
        input = """
        float arr[10];
        void main(int argc, int argv[])
        {
            boolean b;
            b = arr[0] >= 1 || true;
            -(2*4.5) < 1 || !"string";
        }
        """
        expect = "Type Mismatch In Expression: UnaryOp(!,StringLiteral(string))"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_type_mismatch_func_call(self):
        input = """
        float arr[10];
        void main(int argc, int argv[])
        {
            getInt(arr);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(getInt),[Id(arr)])"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_type_mismatch_func_call2(self):
        input = """
        float arr[10],x,y;
        boolean BTS, TXT;
        void main(int argc, int argv[])
        {
            putString(true);
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(putString),[BooleanLiteral(true)])"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_type_mismatch_func_call_passing_array(self):
        input = """
        int arr[10];
        void main(int argc, int argv[])
        {
            test(arr); // OK
            {
                string greets[2];
                test((pointer())); // OK
                test(greets); // Fail
            }
        }
        string yeonjun;
        void test(int arr[]) {
            putInt(arr[0]);
        }

        int[] pointer() {
            int tmp[10];
            return tmp;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(test),[Id(greets)])"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_type_mismatch_func_call_passing_coerced(self):
        input = """
        int arr;
        void main(int argc, int argv[])
        {
            test(arr); // OK
            {
                boolean bool_arr[10];
                test((pointer())); // OK
                test(bool_arr); // Fail
            }
        }

        void test(float arr) {
            putInt(arr);
        }

        int pointer() {
            int tmp;
            tmp = 10;
            return tmp;
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(test),[Id(bool_arr)])"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_type_function_not_return(self):
        input = """
        int arr;
        void main()
        {
            int i, num; string odd_sum , even_sum;
            i = num = -100;
            odd_sum = even_sum = "number";
            float _num;
            _num =10;
            printf("Enter the value of num", "0");
            
            for (num*num; i <= 13.06e13; num+4)
            {
                if (i % 2 == 0)
                    even_sum = even_sum;
                else {
                    float t;
                    t = 0.4499;
                    for(i;994 == 234;i) 
                        odd_sum = even_sum;
                }
            }
        printf("Sum of all odd numbers  = %d\\n", odd_sum);
        printf("Sum of all even numbers = %d\\n", even_sum);
        }

        void printf(string str, string num) {
            putString(str);
            pointer();
        }

        int pointer() {
            int tmp;
            tmp = 10;
        }
        """
        expect = "Function pointer Not Return "
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_type_function_not_return_in_for_loop(self):
        input = """
        int arr;
        int main()
        {
            int i, num; string odd_sum , even_sum;
            i = num = -100;
            
           
            printf("Enter the value of num", "0");
            
            for (num*num; i <= 13.06e13; num+4)
            {
                odd_sum = even_sum = "number";
                float _num;
                _num =10;
                if (i % 2 == 0)
                    even_sum = even_sum;
                else {
                    float t;
                    t = 0.4499;
                    for(i;994 == 234;i) 
                        odd_sum = even_sum;
                }
                return num;
            }
        }

        void printf(string str, string num) {
            putString(str);
            pointer();
        }

        int pointer() {
            int tmp;
            tmp = 10;
            return tmp;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_type_function_not_return_in_one_branch_of_loop(self):
        input = """
        int arr;
        int main()
        {
            int i, num; string odd_sum , even_sum;
            i = num = -100;
            odd_sum = even_sum = "number";
            float _num;
            _num =10;
            printf("Enter the value of num", "0");
            
            {
                if (i % 2 == 0)
                    even_sum = even_sum;
                else {
                    float t;
                    t = 0.4499;
                    for(i;994 == 234;i) 
                        odd_sum = even_sum;
                    return 0;
                }
            }
        }

        void printf(string str, string num) {
            putString(str);
            pointer();
        }

        int pointer() {
            int tmp;
            tmp = 10;
            return tmp;
        }
        """
        expect = "Function main Not Return "
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_type_function_not_return_do_while(self):
        input = """
        int arr;
        int main()
        {
            int i, num; string odd_sum , even_sum;
            i = num = -100;
            odd_sum = even_sum = "number";
            float _num;
            _num =10;

            do
                printf("Enter the value of num", "0");
                if (i % 2 == 0)
                    {even_sum = even_sum; return 1;}
                else {
                    float t;
                    t = 0.4499;
                    for(i;994 == 234;i) 
                        odd_sum = even_sum;
                    return 0;
                }
            while(false);
        }

        void printf(string str, string num) {
            putString(str);
            pointer();
        }

        int pointer() {
            int tmp;
            tmp = 10;
            return tmp;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_type_function_not_return_block(self):
        input = """
        int i,j,k[100];
        int main()
        {
            do
                printf("Enter the value of num", "0");
                if (i % 2 == 0) {
                    for(i;994 == 234;i) 
                        break;
                    return 4499;
                }
                else {
                    float t;
                    t = 0.4499;
                    
                    return 0;
                }
            while(false);
        }

        void printf(string str, string num) {
            putString(str);
            pointer();
        }

        int pointer() {
            int tmp;
            tmp = 10;
            {return tmp;}
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_break_not_in_loop(self):
        input = """
        string arr[2];
        string[] main()
        {
            printf("Input desired number", arr[0]);
            factorial(num);
            return arr;
        }

        void printf(string str, string num) {
            putString(str);
            num = "input nunmber";
        }
        int num;
        int factorial(int n) {
            if (n <= 1)
                return 1;
            else {
                break;
                return n*factorial(n-1);  
            }           
        }
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_continue_not_in_loop(self):
        input = """
        int check_armstrong(int n) {
            int sum, temp;
            int remainder,digits; 
            digits = 0;
   
            temp = n;
 
            do
                digits;
                temp = temp/10;
            while (temp != 0);
   
            temp = n;
            do remainder = temp%10;
                sum = sum + power(remainder, digits)[4*temp-1];
                temp = temp/10;
                break;
            while (temp != 0);

            {continue;} // error here


            if (n == sum)
                return 1;
            else
                return 0;
        }
        void main() {
            check_armstrong(9);
        }
 
        int[]  power(int n, int r) {
            int BTS, Yoongi[3];
            Yoongi[2] = 1;
            int c,p;
            p=10;
            for (c = 1; c <= r; c+1)
                if(true) 
                    continue;
                else
                    p=p*n;
     
            return Yoongi;  
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_no_entry_point(self):
        input = """
        int swap()
        {
            int x, y, t;
            x = 13;
            y = 00000000000000000000000000000000004;
            t = 0;
 
            ("Enter two integers\\n");
            "Before Swapping\\nFirst integer = %d\\nSecond integer = %d\\n"; (x* y);
 
            t = x;
            x = y;
            y = t;
            "After Swapping\\nFirst integer = %d\\nSecond integer = %d\\n"; (x- y) < 49 || !(-(x+y)/3 < 6e25);
 
            return 0;
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,457))
    
    def test_no_entry_point2(self):
        input = """
        void swap(int x, int y)
        {
            int tmp;
            tmp = 0;
            tmp = x;
            x = y;
            y = tmp;
            printRes(x,y,2);
        }

        void printRes(float var1, float var2, int num) {
            putFloat(var1);
            putFloat(var2);
            swap(0,999);
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_unreachable_func(self):
        input = """
        int[] foo() {
            int arr[10];
            return arr;
        }
        void main(int x, int y)
        {
            int tmp;
            tmp = 0;
            tmp = x;
            x = y;
            y = tmp;
            printRes(x,y,2);
        }

        void printRes(float var1, float var2, int num) {
            putFloat(var1);
            putFloat(var2);
            main(0,999);
        }
        """
        expect = "Unreachable Function: foo"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_unreachable_func2(self):
        input = """
        int[] foo() {
            int arr[10];
            return arr;
        }
        int[] main(int x, int y)
        {
            int tmp;
            tmp = 0;
            tmp = x;
            x = y;
            y = tmp;
            return foo();
        }

        void printRes(float var1, float var2, int num) {
            putFloat(var1);
            putFloat(var2);
            printRes(0.e25,999,3);
        }
        """
        expect = "Unreachable Function: printRes"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_not_left_value_literal(self):
        input = """
        void swap(int x, int y)
        {
            int tmp;
            tmp = 0;
            tmp = x;
            x = y;
            y = tmp;
            printRes(x,y,2);
        }

        float global;
        void main(int n)
        {
            swap(1,2);
            int c, result;
            result = 1;
 
            for (c = 1; c <= n; c+1)
                100 = result*c;
 
            return ;
        }

        void printRes(float var1, float var2, int num) {
            putFloat(var1);
            putFloat(var2);
            printRes(0.e25,999,3);
        }
        """
        expect = "Not Left Value: IntLiteral(100)"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_not_left_value_func(self):
        input = """

        float global;
        void main(int n)
        {
            int c, result;
            result = 1;
            printRes(0.5,4.97e01, 4) = 1==1 || true && false;
            for (c = 1; c <= n; c+1)
                result = result*c;
 
            return ;
        }

        boolean printRes(float var1, float var2, int num) {
            putFloat(var1);
            putFloat(var2);
            printRes(0.e25,999,3);
            return true;
        }
        """
        expect = "Not Left Value: CallExpr(Id(printRes),[FloatLiteral(0.5),FloatLiteral(49.7),IntLiteral(4)])"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_not_left_value_func_return_array(self):
        input = """
        void swap(int x, int y)
        {
            int tmp;
            tmp = 0;
            tmp = x;
            x = y;
            y = tmp;
            printRes(x,y,test)[9] = !true || (25*x<=0.5-y); 
        }
        boolean test[2];
        float global;
        void main(int n)
        {
            int c, result;
            result = 1;
            string t;
            t = "string here";
            for (c = 1; c <= n; c+1)
            {
                result = result*c;
                swap(c, result);
            }
 
            return ;
        }

        boolean[] printRes(float var1, float var2, boolean num[]) {
            putFloat(var1);
            putFloat(var2);
            printRes(0.e25,999,test);
            
            return num;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_not_left_value_expr(self):
        input = """
        float flag[10];
        string CTF;
        int main() {
            flag[2] = flag[0]*5 / 59;
            true && !(9 > 4)  = flag[8];
            return 0;
        }
        """
        expect = "Not Left Value: BinaryOp(&&,BooleanLiteral(true),UnaryOp(!,BinaryOp(>,IntLiteral(9),IntLiteral(4))))"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_unreachable_stmt_assign_after_return(self):
        input = """
        int main(){
            foo();
            if(true){
                return 0;
            }
            else{
                return 0;
                a = 9;
            }
        }

        void foo(){

        }
        """
        expect = "Unreachable Statement: BinaryOp(=,Id(a),IntLiteral(9))"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_unreachable_stmt_block_after_return(self):
        input = """
        void main(string CTF){
            float array[5];
            array[4] = 0;
            putString(CTF);
            return;
            {
                // do nothing here
            }
        }
        
        """
        expect = "Unreachable Statement: Block([])"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_unreachable_stmt_return_after_return(self):
        input = """
        boolean main(int a, int b){
            return swap(a, b);
        }

        boolean swap(int x, int y) {
            if (x == y)
                x = x+1;
            else
                {return true;
                return x < y;
                }      
        }
        
        """
        expect = "Unreachable Statement: Return(BinaryOp(<,Id(x),Id(y)))"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_unreachable_stmt_after_break(self):
        input = """
        int main () {

        /* local variable definition */
        int a;
        a = 1;
        /* do loop execution */
        do {
            putString("value of a: %d\\n");
            if (a > 0)
                break;
            else
                break;
            { // This is a block 
                int a;
                {
                    a = 10;
                }
             }
        }while( a < 20 );
 
        return 0;
        }
        """
        expect = "Unreachable Statement: Block([VarDecl(a,IntType),Block([BinaryOp(=,Id(a),IntLiteral(10))])])"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_unreachable_stmt_after_continue(self):
        input = """
        int a;
        int main () {
        if (a> 0){
        do 
        a;
        {
            int b;
            b = 1;
            {
                if (a > 0)
                    break;
                else    
                { // This is a block 
                    continue;
                    a = 10;
                }
            }
        }while( a < 20 );
        }
 
        return 0;
        }
        """
        expect = "Unreachable Statement: BinaryOp(=,Id(a),IntLiteral(10))"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_unreachable_stmt_vardecl_after_continue_noerr(self):
        input = """
        int a;
        int main () {
        if (a> 0){
        do 
        a;
        {
            int b;
            b = 1;
            {
                if (a > 0)
                    break;
                else    
                { // This is a block 
                    continue;
                    int x,y,z;
                }
            }
        }while( a < 20 );
        }
 
        return 0;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_index_out_of_range_idx_equal_size(self):
        input = """
        int i, j, num, temp;

        void main()
        {
            int array[1000];
 
            putLn();
            putString("Enter the elements one by one ");
            for (i = 0; i < num; (i))
            {
                array[i] * array[0] / 4;
            }
            putInt(array[0]);
            for (i = 0; i < num; (array[i]))
            {
                //printf("%d", array[i]);
            }
            /*   Bubble sorting begins */
                for (i = 0; i < num; i)
                {
                    for (j = 0; j < (num - i - 1); j+1)
                    {
                        if (array[j] > array[j + 1])
                    {
                    temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = array[4000]; // error here
                }
            }
        }
        putString("Sorted array is...");
        for (i = 0; i < num; i+-1)
        {
            putString("%d array[i]");
        }
        }
        """
        expect = "Index Out Of Range: ArrayCell(Id(array),IntLiteral(4000))"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_index_out_of_range_calc_idx_const_expr(self):
        input = """
        int i, j, num, temp;

        void main()
        {
            int array[1000];
            putInt(array[j*j*num-temp]); // OK
            for (i = 0; i < num; (array[i]))
            {
                //printf("%d", array[i]);
            }
            /*   Bubble sorting begins */
                for (i = 0; i < num; i)
                {
                    for (j = 0; j < (num - i - 1); j+1)
                    {
                        if (array[j] > array[j + 1])
                    {
                   // temp = array[23.05-9+400];     // OK
                    array[j] = array[j + 1];
                    array[j + 1] = array[25*10/5+1000*9]; // error here
                }
            }
        }
        }
        """
        expect = "Index Out Of Range: ArrayCell(Id(array),BinaryOp(+,BinaryOp(/,BinaryOp(*,IntLiteral(25),IntLiteral(10)),IntLiteral(5)),BinaryOp(*,IntLiteral(1000),IntLiteral(9))))"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_index_out_of_range_array_size_0(self):
        input = """
        int i, j, num, temp;

        void main()
        {
            float array[0];
            for (i = 0; i < num; 400)
            {
                putFloat(array[0]);   // Error here
                if (true)
                    break;
            }          
        }
        """
        expect = "Index Out Of Range: ArrayCell(Id(array),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_index_out_of_range_negative_idx_expr(self):
        input = """
        int i, j, num, temp;

        void main()
        {
            float array[0];
            for (i = 0; i < num; 400)
            {
                putFloat(array[25-99+10]);   // Error here
                if (true)
                    break;
            }          
        }
        """
        expect = "Index Out Of Range: ArrayCell(Id(array),BinaryOp(+,BinaryOp(-,IntLiteral(25),IntLiteral(99)),IntLiteral(10)))"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_index_out_of_range_negative_index(self):
        input = """
        int i, j, num, temp;
        void main()
        {
            boolean array[0];
            {
                {
                    {
                        {
                            putBool(array[-449]);   // Error here
                        }
                    }
                }
                if (true)
                    continue;
            }         
        }
        """
        expect = "Index Out Of Range: ArrayCell(Id(array),UnaryOp(-,IntLiteral(449)))"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_uninitialized_variable(self):
        input = """
        int binary_search(int list[], int lo, int hi, int key)
        {
            int mid;
 
            if (lo > hi)
            {
                int re, ANS, _404_;
                putString("Key not found\\n");
            }
            mid = (lo + hi) / 2;
            if (list[mid] == key)
            {
                putLn();
            }
            else if (list[mid] > key)
            {
                binary_search(list, lo, mid - 1, key);
            }
            else if (list[mid] < key)
            {
                binary_search(list, mid + 1, hi, key);
            }

            return 1;
        }
        int l,h;
        void main() {
            int res; 
            int lst[10];
            int k;
            res = binary_search(lst,l,h,k);
        }
        """
        expect = "Uninitialized Variable: k"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_uninitialized_variable2(self):
        input = """
        
        void main() {
            int main; 
            int lst[10];
            int k;
            k = 10;
            lst[4*k-1]  - main * 99.0000000009;
        }
        """
        expect = "Uninitialized Variable: main"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_uninitialized_variable_inside_block(self):
        input = """
        
        void main() {
            int main; 
            int lst[10];
            int k;
            k = 10;
            {
                int k;
                {
                    main = 000;
                    1 - 25.04 * -.0e98 +(((k))) * main;
                }
            }
        }
        """
        expect = "Uninitialized Variable: k"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_uninitialized_variable_inside_block2(self):
        input = """
        void main() {
            int a,b;
            a = 100;
            define(a, a);
            define(b,b);
        }
        void define(int a, int b) {
            putInt(a);
            float txt[100];
            putFloatLn(txt[9*9]);
        }
        """
        expect = "Uninitialized Variable: b"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_pure_vardecl(self):
        input = """
        int a,x,b,XXX, YYY, __[99],d;
        float ate[000], youtube;
        boolean facebool, twitter[2], yahoo_yayayayay;
        string _name_, _id_;
        string JLPT, _____[1999];
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_pure_funcdecl(self):
        input = """
        void foo() {
            // do this, so that
        }

        int[] random_num_list(int a, int b) {
            int lst[2];
            lst[0] = a;
            lst[1] = a - b;
            return lst;
        }

        boolean main() {
            foo();
            return redundance(random_num_list(44,99));
        }

        boolean redundance(int list[]) {
            if (list[0] != 0)
                return true;
            else
                return !(list[0] <= list[1]);
        } 
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_pure_funcdecl_with_error_in_return(self):
        input = """
        void foo() {
            // do this, so that
        }
        
        int[] random_num_list(int a, int b) {
            int lst[2];
            lst[0] = a;
            lst[1] = a - b;
            return lst;
        }

        boolean main() {
            foo();
            return redundance(random_num_list(44,99)); // Error here
        }

        int redundance(int list[]) {
            if (list[0] != 0)
                return 0;
            else
                return -(list[0]-list[1]);
        } 
        """
        expect = "Type Mismatch In Statement: Return(CallExpr(Id(redundance),[CallExpr(Id(random_num_list),[IntLiteral(44),IntLiteral(99)])]))"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_no_error_program(self):
        input = """
        int i;
        int f() {
            return 200;
        }
        void main() {
            int main;
            main = f();
            putIntLn(main);
            {
                int i;
                int main;
                int f;
                main = f = i = 100;
                putIntLn(i);
                putIntLn(main);
                putIntLn(f);
            }
            putIntLn(main);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_type_mismatch_in_compare_string(self):
        input = """
        string str[100];
        string[] main ()
        {
            int c; c = 0;
            string ch, s[1000];
   
        do 
            ch = s[c];
            if (ch >= "A" && ch <= Z)
                s[c] = s[c] + 32;
            else if (ch >= a && ch <= char[z])
                s[c] = s[c] - 32;  
            c+1;  
        while (s[c] != 0);
        return "completed";
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(>=,Id(ch),StringLiteral(A))"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_error_use_var_ass_func(self):
        input = """
        void main( int a[], int var )
        {
            int k, i, l, j;
            i=j=99;
            k=l=i-9*j;
 
            for ( k = 0;k < var;k() )   //error here
            {
                for ( i = 0;i <= var;i )
                {
                    l = (a[ i ])-a[ k ];
 
                    for ( j = 0;j <= var;j )
                    {
                        if ( i != k )
                            a[j] = a[a[k]*a[j]-(l*a[k])];
                    }
                }
            }
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(k),[])"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_break_in_nested_for_loop(self):
        input = """
        void main( int a[], int var )
        {
            int k, i, l, j;
            i=j=99;
            k=l=i-9*j;
 
            for ( k = 0;k < var;k )   //error here
            {
                for ( i = 0;i <= var;i )
                {
                    l = (a[ i ])-a[ k ];

                    {
                        {
                            break;
                        }
                    }
 
                    for ( j = 0;j <= var;j )
                    {
                        if ( i != k )
                            a[j] = a[a[k]*a[j]-(l*a[k])];
                    }
                }
            }
        }
        """
        expect = "Unreachable Statement: For(BinaryOp(=,Id(j),IntLiteral(0));BinaryOp(<=,Id(j),Id(var));Id(j);Block([If(BinaryOp(!=,Id(i),Id(k)),BinaryOp(=,ArrayCell(Id(a),Id(j)),ArrayCell(Id(a),BinaryOp(-,BinaryOp(*,ArrayCell(Id(a),Id(k)),ArrayCell(Id(a),Id(j))),BinaryOp(*,Id(l),ArrayCell(Id(a),Id(k)))))))]))"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_type_mismatch_in_dowhile(self):
        input = """
        string a,b,x,__;
        int main(string argv[], int argc) { do do {} while(__); while(true); }
        int minDistance(int dist[], int sptSet[]) { 
            if (_) return dist[0];
        } 
        float b1, c, XXX, YYY, ___[343434343], hcmut, edu;
        boolean _b, c2, X0XX, YY8Y, _3__[343434343], h6cmut, ed2u;
        """
        expect = "Type Mismatch In Statement: Dowhile([Block([])],Id(__))"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_undeclared_func_in_dowhile(self):
        input = """
        string a,b,x,__;
        int main(string argv[], int argc) { do do {} while(isDone(__)); while(true); }
        int minDistance(int dist[], int sptSet[]) { 
            if (_) return dist[0];
        } 
        float b1, c, XXX, YYY, ___[343434343], hcmut, edu;
        boolean _b, c2, X0XX, YY8Y, _3__[343434343], h6cmut, ed2u;
        """
        expect = "Undeclared Function: isDone"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_many_if_else(self):
        input = """
        void main(int a[], int m, int b[], int n, int sorted[]) {
            int i, j, k;
            j = k = 0;
 
            for (i = 0;check(true);m+n) {
                if (j < m && k < n) {
                    if (a[j] < b[k]) {
                        sorted[i] = a[j];
                        j + 1;
                    }
                    else {
                        sorted[i] = b[k];
                        k+2;
                    }
                    i+0;
                }
                else if (j == m) {
                    for (i; i < m + n;(a[9])) {
                        sorted[i] = b[k];
                    }
                    continue;
                }
                else {
                    for (m; i < m + n;a[2*5-m+0]) {
                        sorted[i] = a[j];
                        break;
                    }
                }
            }
        }
        boolean check(boolean t) {
            return t;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_undeclared_var_in_dowhile(self):
        input = """
        string a,b,x,__;
        int main(string argv[], int argc) { do do {} while(_b); a = greets_from_os; while(true); }
        int minDistance(int dist[], int sptSet[]) { 
            if (_) return dist[0];
        } 
        float b1, c, XXX, YYY, ___[343434343], hcmut, edu;
        boolean _b, c2, X0XX, YY8Y, _3__[343434343], h6cmut, ed2u;
        """
        expect = "Undeclared Identifier: greets_from_os"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_unreachable_stmt_due_to_continue_else_branch(self):
        input = """
        void main(int a[], int m, int b[], int n, int sorted[]) {
            int i, j, k;
            j = k = 0;
 
            for (i = 0;check(true);m+n) {
                if (j < m && k < n) {
                    if (a[j] < b[k]) {
                        sorted[i] = a[j];
                        j + 1;
                    }
                    else {
                        sorted[i] = b[k];
                        k+2;
                    }
                    i+0;
                }
                else if (j == m) {
                    continue;                       // Error here
                    for (i; i < m + n;(a[9])) {
                        sorted[i] = b[k];
                    }
                    
                }
                else {
                    for (m; i < m + n;a[2*5-m+0]) {
                        sorted[i] = a[j];
                        break;
                    }
                }
            }
        }
        boolean check(boolean t) {
            return t;
        }
        """
        expect = "Unreachable Statement: For(Id(i);BinaryOp(<,Id(i),BinaryOp(+,Id(m),Id(n)));ArrayCell(Id(a),IntLiteral(9));Block([BinaryOp(=,ArrayCell(Id(sorted),Id(i)),ArrayCell(Id(b),Id(k)))]))"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_unreachable_stmt_due_to_break_else_branch(self):
        input = """
        void main(int a[], int m, int b[], int n, int sorted[]) {
            int i, j, k;
            j = k = 0;
 
            for (i = 0;check(true);m+n) {
                if (j < m && k < n) {
                    if (a[j] < b[k]) {
                        sorted[i] = a[j];
                        j + 1;
                    }
                    else {
                        sorted[i] = b[k];
                        k+2;
                        break;          
                    }
                     
                    i+0;
                }
            }
        }
        boolean check(boolean t) {
            return t;
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_unreachable_stmt_due_to_breakandcontinue_all_branch(self):
        input = """
        void main(int a[], int m, int b[], int n, int sorted[]) {
            int i, j, k;
            j = k = 0;
 
            for (i = 0;check(true);m+n) {
                if (j < m && k < n) {
                    if (a[j] < b[k]) {
                        sorted[i] = a[j];
                        j + 1;
                        continue;
                    }
                    else {
                        sorted[i] = b[k];
                        k+2;
                        break;             
                    }
                     
                    i+0; // Error here 
                }
            }
        }
        boolean check(boolean t) {
            return t;
        }
        """
        expect = "Unreachable Statement: BinaryOp(+,Id(i),IntLiteral(0))"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_not_left_value_expr_in_dowhile(self):
        input = """
        string Exp, Mana, mana[0]; 
        int Array[10], PPL_test[100];
        int main(string argv[], int argc) { 
            string tmp[2];
            PPL(tmp);
            if (PPL_test[4] > 0)
                return Array[007]*0;
            return 0;
        }
        string[] PPL(string s[]) {
            do 
                PPL_test[10] + Array[PPL_test[0]] = "Go go go!!!"; // error here
            while (CSE[1]);
            return mana;
        }
        boolean HCMUT, CSE[2], VNU;
        string FourIV;
        float _01,Finish,_;
        
        """
        expect = "Not Left Value: BinaryOp(+,ArrayCell(Id(PPL_test),IntLiteral(10)),ArrayCell(Id(Array),ArrayCell(Id(PPL_test),IntLiteral(0))))"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_type_mismatch_in_return_stmt(self):
        input = """
        string Exp, Mana, mana[1]; 
        int Array[10], PPL_test[100];
        int main(string argv[], int argc) { 
            string tmp[2];
            PPL(tmp);
            if (PPL_test[4] > 0)
                return Array[007]*0;
            return 0;
        }
        string[] PPL(string s[]) {
            do 
                mana[Array[PPL_test[0]]] = "Go go go!!!"; 
            while (CSE[1]);
            return Mana;    // Error here
        }
        boolean HCMUT, CSE[2], VNU;
        string FourIV;
        float _01,Finish,_;
        
        """
        expect = "Type Mismatch In Statement: Return(Id(Mana))"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_unreachable_function2(self):
        input = """
        int main(string argv[], int argc) { return 0;  }
        float solve_for_y(float a, float b, float c)
        {
            float Y;
            if(a <= 0) {
                putStringLn("Value of Y cannot be predicted");
            }
            else {
                Y = -(b + c) / a;
            }
            return Y;
        }
        """
        expect = "Unreachable Function: solve_for_y"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_unreachable_function_self_called(self):
        input = """
        int compare_strings(string a[], string b[])
        {
            int c; c = 0;
            int _a[2], _b[9];
            do {}
                if (_a[c] == 0 || _b[c] < 0)
                {
                    for(c;c==0;c) {
                        compare_strings(a,b);
                    }
                    break;
                }
            while (_a[c] == _b[c]);           
   
            if (_a[c] == 404 && _b[c] == c)
                return 0;
            else
                return -1;
        }
        void main() {}
        """
        expect = "Unreachable Function: compare_strings"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_uninitialized_var_pass_to_func(self):
        input = """
        float global;
        void factorial(int n)
        {
            int c;
            float result;
            result = 1;
 
            for (c = 1; c <= n; c+9)
                result = result*global;
 
            return ;
        }
        void main() {
            int n;
            factorial(n);    // Error here
        }
        """
        expect = "Uninitialized Variable: n"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_uninitialized_var_pass_to_func(self):
        input = """
        string _Deadline;
        int segment[100];
        void PPL(float Assignment, int status)
        {
            int progress;
            int i;
            i = 0;

            do
                for (progress = 0; !pending(progress); progress = progress+1) {
                    _Deadline = "Coming close...";
                    i = i+1;
                }

                Assignment = progress*segment[i] - 10;
                if (Assignment > 100.0e-010)
                {
                    status = segment[99]+400/100;
                    break;
                }
            while(true);
        }
        string main() {
            string _PPL_;
            _PPL_ = "PPL is Done :>";
            {{
                {
                    float t;
                    int b;
                    t = b = 0;
                    PPL(t, b);
                }
            }}
            return "PPL is Awesome!!!";
        }
        boolean pending(int will) {
            if (will == 1) 
                return true;
            else
                return !(true);
        }
        """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,499))

    


    
    

    
    

    

    

    

    
    

    


    



    
   

    
    

   