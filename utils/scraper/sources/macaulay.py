from .base import BaseSource
import requests
import json
from typing import Optional, Dict, List, Any

class MacaulaySource(BaseSource):
    def __init__(self):
        super().__init__("macaulay")
        self.base_url = "https://search.macaulaylibrary.org/api/v1/search"
        self.supported_qualities = ["A", "B", "C", "D"]
    
    def search(self, species: str, quality: Optional[str] = None,
               limit: Optional[int] = 50, **kwargs) -> List[Dict]:
        """Search Macaulay Library for recordings"""
        params = {
            'q': species,
            'mediaType': 'audio',
            'sort': 'rating_rank_desc',
        }
        
        if quality:
            params['quality'] = quality
        if limit:
            params['count'] = limit
        
        response = requests.get(self.base_url, params=params)
        data = response.json()
        
        return data.get('results', {}).get('content', [])
    
    def download(self, recording_info: Dict, download_dir: str) -> bool:
        """Download from Macaulay Library"""
        # Implementation depends on Macaulay Library API structure
        # This is a placeholder - you'd need to check their actual API
        asset_id = recording_info.get('assetId')
        common_name = recording_info.get('commonName', 'Unknown')
        scientific_name = recording_info.get('scientificName', '')
        
        filename = f"ML{asset_id} - {common_name} - {scientific_name}.mp3"
        filename = self.clean_filename(filename)
        
        # Actual download implementation would go here
        print(f"Would download: {filename}")
        return True
    
    def validate_quality(self, quality: str) -> bool:
        return quality in self.supported_qualities