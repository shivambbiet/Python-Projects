const API_URL = "http://localhost:5000";

export const uploadProduct = async (formData) => {
  const res = await fetch(`${API_URL}/products/upload`, {
    method: "POST",
    body: formData,
  });
  return res.json();
};

export const getProducts = async () => {
  const res = await fetch(`${API_URL}/products/`);
  return res.json();
};