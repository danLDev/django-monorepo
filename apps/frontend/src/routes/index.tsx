import { DeckGL } from '@deck.gl/react';
import type { MapViewState } from '@deck.gl/core';
import { GeoJsonLayer } from '@deck.gl/layers';
import { createFileRoute, useNavigate } from '@tanstack/react-router';
import { useQuery } from '@tanstack/react-query';
import type { Studio } from '@/types';



const COUNTRIES = 'https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_admin_0_scale_rank.geojson'; //eslint-disable-line

export const Route = createFileRoute('/')({ component: App })

const INITIAL_VIEW_STATE: MapViewState = {
  longitude: -122.41669,
  latitude: 37.7853,
  zoom: 13
};



function App() {

  const { data } = useQuery<{ results: Studio[] }>({
    queryKey: ['studios'],
    queryFn: () => fetch('http://localhost:8000/studios').then(res => res.json()),
  })



  const navigate = useNavigate()

  const features = (data?.results ?? []).map((studio) => ({
    type: 'Feature',
    properties: {
      name: studio.description,
      owner: studio.owner,
      id: studio.id
    },
    geometry: studio.location_geojson
  }));


  const layers = [
    new GeoJsonLayer({
      id: 'base-map',
      data: COUNTRIES,
      stroked: true,
      filled: true,
      lineWidthMinPixels: 2,
      opacity: 0.4,
      getLineColor: [60, 60, 60],
      getFillColor: [200, 200, 200]
    }),
    new GeoJsonLayer({
      id: 'studios',
      data: {
        type: 'FeatureCollection',
        features: features as any
      },
      filled: true,
      pointRadiusMinPixels: 2,
      pointRadiusScale: 2000,
      getPointRadius: (f) => 30,
      highlightColor: [204, 116, 91, 180],
      pickable: true,
      autoHighlight: true,
      getFillColor: [245, 107, 69, 180],
      onClick: (info) => info.object && navigate({ to: '/studio/$id', params: { id: info.object.properties.id } })
    })
  ];

  return <DeckGL
    initialViewState={INITIAL_VIEW_STATE}
    controller
    layers={layers} />;
}