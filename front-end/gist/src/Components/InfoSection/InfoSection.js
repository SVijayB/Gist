import './InfoSection.css'
import Pic1 from '../../Images/vj1.jpg'
import Pic2 from '../../Images/naveen.jpg'
import Pic3 from '../../Images/santosh.jpg'


function InfoSection(props){
 
   return (
    <>
    <div className="AboutProjectSection" id="AboutSection">
        <div className="AbtText size1 center-text">
           About Project
        </div>
        <div className="AbtText size2 center-text">
            <p>
                Our project focuses on creating an accurate text summarizer for news articles. We developed an API that uses various NLP models to acquire a summary of an entire news article. While the API can be potentially used for various other cases including, Movie and book summaries, e-commerce product review summaries, and so on.
                Our product Gist focuses on a small part of it for newspaper summarization. This is why we have open-sourced our project for it to be used by people as per their requirements and scope.
                The main difference between our summarizer and other summarizers already in the market is that ours is an abstractive type rather than extractive, which means, it focuses on creating and framing it's own summaries rather than just focusing on points which are relevant and copy pasting them in the summary.
            </p>
        </div>
    </div>

     
    <div className="infoseaction">
        <div className="Team" id="team">
              Meet Our Team
        </div>
        <div className="flex_list">
                <div className="User_Imgs">
                  <div className="DImg">
                    <img src={Pic1} alt="PIC" />
                  </div>
                </div>
                <div className="User_Imgs">
                  <div className="DImg">
                    <img src={Pic2} alt="PIC" />
                  </div>
                </div>
                <div className="User_Imgs">
                  <div className="DImg">
                    <img src={Pic3} alt="PIC" />
                  </div>
                </div>
        </div>
    </div>
   </>);


}


export default InfoSection;