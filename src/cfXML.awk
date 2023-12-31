BEGIN { start = 0 }
$0 ~ "# Concrete Nodes" { start = 1; print; next }
!start { print; next }
start && $0 ~ "def XML\\(self, indentLevel" { 
  $0 = "    def XML(self, indentLevel=0, syntax=\"XML\", field=\"children\"):";
  print ; next }
start && $0 ~ "result \\+= '<" {
  print;
  print "        if field != \"children\": result += \" containerField='\" + field + \"'\"";
  next; }
start && $0 ~ "result \\+= self.metadata.XML\\(indentLevel=indentLevel\\+1, syntax=syntax\\)" {
  print "                result += self.metadata.XML(indentLevel=indentLevel+1, syntax=syntax, field=\"metadata\")";
  next; }
start && $0 !~ "self.IS" && $0 !~ "self.metadata" && $0 ~ "# output this SFNode" {
  SFNodeNR = NR;
  field = substr($2, 6);
  sub(":", "", field);  
  print; next; }
start && NR == SFNodeNR + 1 && $0 ~ "XML\\(" {
   sub(")", ", field=\"" field "\")");
   print; next; }
start && $0 ~ "# walk each child in list, if any \\(avoid empty list recursion\\)" {
  MFNodeNR = NR;
  field = substr($2, 6);
  sub(":", "", field);  
  print; next; }
start && NR == MFNodeNR + 2 && $0 ~ "result \\+= each.XML\\(indentLevel=indentLevel\\+1, syntax=syntax\\)" {
  sub(")", ", field=\"" field "\")");
  print; next; }
{print}