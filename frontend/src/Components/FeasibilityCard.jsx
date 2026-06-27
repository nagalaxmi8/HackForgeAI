import { CheckCircle, AlertTriangle, Lightbulb, Rocket } from "lucide-react";
import { renderValue } from "../utils/renderValue";

function FeasibilityCard({ data }) {
  if (!data) return null;

  return (
    <div className="card">

      <div className="feasibility-header">

        <div>
          <h2 className="card-title">📊 Feasibility Analysis</h2>
          <p>AI evaluation of your project idea.</p>
        </div>

        <div className="score-circle">
          <h1>{data.score}</h1>
          <span>/100</span>
        </div>

      </div>

      <div className="complexity-pill">
        ⚡ {data.complexity} Complexity
      </div>

      <div className="feasibility-grid">

        <div className="mini-card">

          <h3>
            <CheckCircle size={18}/>
            Advantages
          </h3>

          <ul>

            {data.pros?.slice(0,3).map((item,index)=>(

              <li key={index}>{renderValue(item)}</li>

            ))}

          </ul>

        </div>

        <div className="mini-card">

          <h3>
            <AlertTriangle size={18}/>
            Challenges
          </h3>

          <ul>

            {data.cons?.slice(0,3).map((item,index)=>(

              <li key={index}>{renderValue(item)}</li>

            ))}

          </ul>

        </div>

      </div>

      <div className="recommend-card">

        <Lightbulb size={22}/>

        <div>

          <h3>Recommendation</h3>

          <p>{data.recommendation}</p>

        </div>

      </div>

      <div className="mvp-card">

        <h3>
          <Rocket size={18}/>
          MVP Stack
        </h3>

        <div className="mvp-tags">

          {data.mvp_features?.slice(0,4).map((item,index)=>(

            <span key={index}>

              {renderValue(item)}

            </span>

          ))}

        </div>

      </div>

    </div>
  );
}

export default FeasibilityCard;