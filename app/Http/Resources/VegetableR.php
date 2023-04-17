<?php

namespace App\Http\Resources;

use Illuminate\Http\Request;
use Illuminate\Http\Resources\Json\JsonResource;

class Vegetable extends JsonResource
{
    /**
     * Transform the resource into an array.
     *
     * @return array<string, mixed>
     */
    public static $wrap='vegetables';
    public function toArray(Request $request): array
    {
       
        return [
            'naziv' => $this->resource->naziv,
            'temperatura' => $this->resource->temperatura,
            'vlaznost_vazduha' => $this->resource->vlaznost_vazduha,
            'temperatura_zemljista' => $this->resource->temperatura_zemljista,

        ];
    }
}
