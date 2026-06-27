import { renderValue } from "../utils/renderValue";
import {
  Monitor,
  Server,
  Database,
  Brain,
  Cloud,
  ArrowRight,
} from "lucide-react";

function ArchitectureCard({ data }) {
  if (!data) return null;

  const architecture = [
    {
      title: "Frontend",
      icon: <Monitor size={22} />,
      value: data.frontend,
    },
    {
      title: "Backend",
      icon: <Server size={22} />,
      value: data.backend,
    },
    {
      title: "Database",
      icon: <Database size={22} />,
      value: data.database,
    },
    {
      title: "AI Model",
      icon: <Brain size={22} />,
      value: data.ai_model,
    },
    {
      title: "Deployment",
      icon: <Cloud size={22} />,
      value: data.deployment,
    },
  ];

  return (
    <div className="card">

      <div className="architecture-header">

        <div>

          <h2 className="card-title">
            🏗 Recommended Architecture
          </h2>

          <p>Suggested technology stack for your project.</p>

        </div>

      </div>

      <div className="architecture-grid">

        {architecture.map((item, index) => (

          <div className="tech-card" key={index}>

            <div className="tech-icon">
              {item.icon}
            </div>

            <h3>{item.title}</h3>

            <p>{renderValue(item.value)}</p>

          </div>

        ))}

      </div>

      <div className="flow-section">

        <h3>⚡ System Workflow</h3>

        <div className="flow-container">

          {data.flow?.map((step, index) => (

            <div className="flow-box" key={index}>

              <div className="flow-number">
                {index + 1}
              </div>

              <div className="flow-text">

                {typeof step === "string" ? (

                  <p>{step}</p>

                ) : (

                  Object.entries(step).map(([key, value]) => (

                    <p key={key}>
                      {renderValue(value)}
                    </p>

                  ))

                )}

              </div>

              {index !== data.flow.length - 1 && (
                <ArrowRight className="flow-arrow" size={20} />
              )}

            </div>

          ))}

        </div>

      </div>

    </div>
  );
}

export default ArchitectureCard;