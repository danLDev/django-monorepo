export type Studio = {
  id: number,
  description: string,
  created_at: string,
  location_geojson: GeoJSON.Point,
  max_capacity: 4,
  image_url?: string,
  owner: number,
};

export type Owner = {
  id: number,
  username: string,
  email: string,
};