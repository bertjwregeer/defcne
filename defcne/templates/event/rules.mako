<%inherit file="../site.mako" />

<%block name="maincontent">
<h1>Create Contest or Event</h1>


<div class="container-fluid">
    <div class="row-fluid">
        <div class="span12">
            <p>Before going on, there are a couple guidelines and tips that we ask you to read.</p>
<h3>Tips, Guidelines, and Gotcha's</h3>

<ol>
<li>This year there ARE additional resources to help the events & contests with costs of expanding and becoming bigger and better. So you have an earth shattering idea but your tight on cash, submit your idea and tell me how we can help.</li>

<li>As with previous years, there will be changes in which contests get a Black Badge. Please don't advertise that you're getting one until I've given you the confirmation. Contests that do not use their space creatively are likely candidates to lose their Black Badge status. Contests that are very popular and get the most attention are good candidates to receive a Black Badge. Newer contests have lesser chance of a Black Badge as well, if it's your first year you will REALLY have to knock it out of the park to get a Black Badge (it's only happened once).</li>

<li>We will have a pre-con contest meeting (Thursday before Con) for the contest and event Points Of Contact (POCs). You need to be there, and if you absolutely can't attend, you will need to let me know well in advance. This meeting is where we will discuss any last minute changes, introduce you to the goon staff, set ground rules, and get you your contest badges. If you fail to attend this meeting or you don't let me know that you will be absent your contest or event will be cancelled and your space awarded to one of the many people who would be happy to have it.</li>

<li>Please fill out the entire form. If there are additional requests, favors owed, comments or other important commitments, please let me know when you submit this form. All RFI's must be submitted by May 1st (NO EXCEPTIONS).</li>

<li>Please make provisions to bring your own prizes to give away this year. Hit up the various vendors and tell them that it's for DEF CON, you might be surprised by how giving they are. It's best to come prepared so no one is disappointed.</li>

<li>This year all "official contests" will receive two contest badges, and approved "unofficial contests" will receive two human badges. If you are a large official contests/event you may need to request additional badges for your support staff. Please make this request in the "OTHER" section of the RFI. Once your contest / event has been selected for DEF CON 20, your badge requests will be reviewed by the C&E Goon Staff and our recommendations will be turned over to The Dark Tangent for his final approval.</li>

<li>The Contest Description, Name, and POC name will all be included in the DEF CON program, so please ensure it's how you like it. If you don't give me your information in plenty of time, you will not be included in the program, and that would just be sad.</li>

<li>Please provide links to any webpages, Facebook page, Twitter names, Flicker feeds, etc. Like last year, we are going to help promote contests with the DEF CON Facebook page and Twitter feed. If you will be tweeting updates please let us know. We will create a Twitter list so attendees can easily follow all the action, and provide constant Facebook updates. Be sure to get on that list!</li>

<li>Remember that you will need to be creative with your space and bring your own signs, booth gear, decorations, etc. You may NOT put anything on the conference area walls and you may not bolt anything to the floor. Once approved, remember to check the secret forum for conference space rules and regulations.</li>

<li>You are NOT allowed to sell ANYTHING at your tables, Period. If you want to sell something, you need to contact the Vendor Dept. Head, Roamer (Roamer (AT) DEF CON (Dot) org) for information on the Vendor Area, or speak with an already approved Vendor to share space. If you are a non-profit (HACKER SPACES PAY ATTENTION!) and you would like to discuss fund raising options please contact me directly.</li>

<li>You will be asked to provide continuous updates about your contest to the Info Booth via paper forms that will be provided to you at the Pre-Con meeting.</li>

<li>As a reminder you will need to find me (Pyr0) and provide a final score and update for your contest NO LATER THAN 2PM ON SUNDAY AFTERNOON, FINAL DAY OF DEF CON. I will need it written or typed on a 8.5" x 11" piece of paper. These final scores and updates will also be what show up on the DEF CON website at the end of the conference, so ensure it says what you want it to say.</li>

<li>In order to accommodate you being allowed early access to the contest area, I will need the REAL names of your people, along with a clear digital picture (roughly 100x100dpi) that I can give to hotel security. They will be checking ID's and if your name isn't on the list you won't be getting into the space.</li>

<li>Official contests are contests that have been approved and vetted. If this is your first year and you are selected, expect to be an "unofficial contest or event". Only approved "official" contests are eligible for Black Badge status, contest badges, and other special events. If it is your first year and you REALLY bring it, The Dark Tangent or Pyr0 might switch your status (at the closing ceremonies) so that you can qualify for these perks.</li>

        </div>
    </div>
    <div class="row-fluid">
        <div class="span12" style="text-align: center;">
            <h3>Do you have what it takes to run a contest or event?</h3>
        </div>
    <div class="row-fluid">
        <div class="span6" style="text-align: center;">
            <a href="${request.route_url('defcne.e', traverse='create/letsgo')}" class="btn btn-primary">Let's get this thing started!</a>
        </div>
        <div class="span6" style="text-align: center;">
            <a href="${request.route_url('defcne')}" class="btn">Nevermind. No longer interested!</a>
        </div>
    </div>
</div>


</%block>

<%block name="title">${parent.title()} - Create Contest or Event</%block>