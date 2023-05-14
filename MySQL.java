public abstract class MySQL {
  
}

Class.forName("com.mysql.cj.jdbc.Driver");
Connection conn = DriverManager.getConnection(
  "jdbc:mysql://gcp.connect.psdb.cloud/cosinemudbox?sslMode=VERIFY_IDENTITY",
  "3kdh65j6seo7b40ozagj",
  "pscale_pw_wLXGfYMXrF5FBu8eNRLx6fWOMER70z5qqxS6fFzuxv5");
