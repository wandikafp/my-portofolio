import math
from projects.smart_shopper.config import get_database_connection, get_embedding_model

db = get_database_connection()
embedding_model = get_embedding_model()

def clean_nan(obj):
    if isinstance(obj, dict):
        return {k: clean_nan(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [clean_nan(v) for v in obj]
    elif isinstance(obj, float) and math.isnan(obj):
        return None
    return obj

def get_product_info(semantic_query: str, category: str = None, max_price: float = None, material: str = None, gender: str = None) -> list:
    """Mencari produk berdasarkan query semantik, kategori, harga maksimal, material, dan gender."""
    query_vector = embedding_model.encode(semantic_query).tolist()
    
    vector_filter = []
    if category: vector_filter.append({"category": {"$eq": category}})
    if max_price: vector_filter.append({"price": {"$lte": max_price}})
    if material: vector_filter.append({"material": {"$eq": material}})
    if gender: vector_filter.append({"gender": {"$eq": gender}})
        
    try:
        vector_search_stage = {
            "$vectorSearch": {
                "index": "vector_index",
                "path": "embedding",
                "queryVector": query_vector,
                "numCandidates": 50,
                "limit": 5
            }
        }
        if vector_filter:
            vector_search_stage["$vectorSearch"]["filter"] = {"$and": vector_filter}
            
        pipeline = [vector_search_stage, {"$project": {"_id": 0, "embedding": 0}}]
        results = list(db.products.aggregate(pipeline))
        if not results: raise Exception("Empty vector search results")
            
    except Exception:
        match_stage = {"$text": {"$search": semantic_query}}
        if category: match_stage["category"] = {"$regex": category, "$options": "i"}
        if max_price: match_stage["price"] = {"$lte": max_price}
        if material: match_stage["material"] = {"$regex": material, "$options": "i"}
        if gender: match_stage["gender"] = {"$regex": f"^{gender}$", "$options": "i"}
        results = list(db.products.find(match_stage, {"_id": 0, "embedding": 0}).limit(5))
        
    return clean_nan(results)

def get_material_safety(material_name: str) -> dict:
    """Mengecek informasi material untuk aspek keamanan/keberlanjutan."""
    result = db.material.find_one({"name": material_name}, {"_id": 0})
    return clean_nan(result) if result else {}
