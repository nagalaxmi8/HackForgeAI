import { renderValue } from "../utils/renderValue";

function TaskCard({ data }) {
  if (!data) return null;

  return (
    <div className="card">
      <h2 className="card-title">👥 Team Task Allocation</h2>

      <div className="task-grid">

        {Object.entries(data).map(([member, tasks]) => (

          <div className="member-card" key={member}>

            <h3>{member.replace("_", " ").toUpperCase()}</h3>

            {/* If tasks is an array */}
            {Array.isArray(tasks) ? (

              <ul>
                {tasks.map((task, index) => (
                  <li key={index}>
                    {typeof task === "string" ? (
                      <>✅ {task}</>
                    ) : (
                      Object.entries(task).map(([key, value]) => (
                        <p key={key}>
                          <strong>{key}:</strong> {renderValue(value)}
                        </p>
                      ))
                    )}
                  </li>
                ))}
              </ul>

            ) : (

              <div>

                {Object.entries(tasks).map(([key, value]) => (

                  <div key={key}>

                    <strong>{key}</strong>

                    {Array.isArray(value) ? (
                      <ul>
                        {value.map((item, i) => (
                          <li key={i}>✅ {renderValue(item)}</li>
                        ))}
                      </ul>
                    ) : (
                      <p>{renderValue(value)}</p>
                    )}

                  </div>

                ))}

              </div>

            )}

          </div>

        ))}

      </div>

    </div>
  );
}

export default TaskCard;