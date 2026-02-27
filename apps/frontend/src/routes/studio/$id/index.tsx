import type { Owner, Studio } from '@/types';
import { useQuery } from '@tanstack/react-query';
import { createFileRoute } from '@tanstack/react-router';


export const Route = createFileRoute('/studio/$id/')({ component: App, })


function App() {

  const { id } = Route.useParams();

  const { data } = useQuery<Studio>({
    queryKey: ['studio', id],
    queryFn: () => fetch(`http://localhost:8000/studios/${id}`).then(res => res.json()),
  })


  const { data: owner } = useQuery<Owner>({
    queryKey: ['owner', data?.owner],
    queryFn: () => fetch(`http://localhost:8000/owners/${data?.owner}`).then(res => res.json()),
    enabled: !!data?.owner,
  })




  return <div>Description: {data?.description} Owner: {owner?.email}</div>
}