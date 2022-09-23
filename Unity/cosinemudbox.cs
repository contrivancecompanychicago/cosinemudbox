PM> Install-Package Postmark

// Import:
using PostmarkDotNet;

// Send an email asynchronously:
var message = new PostmarkMessage()
{
  To = "erichilarysmith@outlook.com",
  From = "support@ericyellowscreencomputers.com",
  TrackOpens = true,
  Subject = "A complex email",
  TextBody = "Hello dear Postmark user.",
  HtmlBody = "<strong>Hello</strong> dear Postmark user. <img src="cid:embed_name.jpg"/>",
  MessageStream = "outbound",
  Tag = "New Year's Email Campaign",
  Headers = new HeaderCollection{
    {"X-CUSTOM-HEADER", "Header content"}
  }
};

var imageContent = File.ReadAllBytes("test.jpg");
message.AddAttachment(imageContent, "test.jpg", "image/jpg", "cid:embed_name.jpg");

var client = new PostmarkClient("097af2c1-cae7-4a71-b821-ac3bc50c4947");
var sendResult = await client.SendMessageAsync(message);

if (sendResult.Status == PostmarkStatus.Success){ /* Handle success */ }
else { /* Resolve issue.*/ }
