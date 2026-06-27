export function renderValue(value) {
    if (value === null || value === undefined) {
      return "-";
    }
  
    if (typeof value === "string") {
      return value;
    }
  
    if (typeof value === "number") {
      return value;
    }
  
    if (typeof value === "boolean") {
      return value ? "Yes" : "No";
    }
  
    if (Array.isArray(value)) {
      return value.join(", ");
    }
  
    if (typeof value === "object") {
      return JSON.stringify(value, null, 2);
    }
  
    return String(value);
  }