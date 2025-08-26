BEGIN { start = 0 }
$0 ~ "# Concrete Nodes" { start = 1; print; next }
$0 ~ "# Field Types" { start = 2; print; next }
$0 ~ "# Statements" { start = 3; print; next }
start == 0 { print; next }
start == 3 && $0 ~ "def XML\\(self, indentLevel" { 
  $0 = "    def XML(self, indentLevel=0, syntax=\"XML\", field=None):";
  print ; next }
start == 2 && $0 ~ "def XML\\(self\\):" { 
  $0 = "    def XML(self, field=None):";
  print ; next }
start == 1 && $0 ~ "def XML\\(self, indentLevel" { 
  $0 = "    def XML(self, indentLevel=0, syntax=\"XML\", field=\"children\"):";
  print ; next }
start == 1 && $0 ~ "result \\+= '<" {
  print;
  print "        if field != \"children\": result += \" containerField='\" + field + \"'\"";
  next; }
start == 1 && $0 ~ "result \\+= self.metadata.XML\\(indentLevel=indentLevel\\+1, syntax=syntax\\)" {
  print "                result += self.metadata.XML(indentLevel=indentLevel+1, syntax=syntax, field=\"metadata\")";
  next; }
start == 1 && $0 !~ "self.IS" && $0 !~ "self.metadata" && $0 ~ "# output this SFNode" {
  SFNodeNR = NR;
  field = substr($2, 6);
  sub(":", "", field);  
  print; next; }
start == 1 && NR == SFNodeNR + 1 && $0 ~ "XML\\(" {
   sub(")", ", field=\"" field "\")");
   print; next; }
start == 1 && $0 ~ "# walk each child in list, if any \\(avoid empty list recursion\\)" {
  MFNodeNR = NR;
  field = substr($2, 6);
  sub(":", "", field);  
  print; next; }
start == 1 && NR == MFNodeNR + 2 && $0 ~ "result \\+= each.XML\\(indentLevel=indentLevel\\+1, syntax=syntax\\)" {
  sub(")", ", field=\"" field "\")");
  print; next; }
{print}
