<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class vegetable extends Model
{
    use HasFactory;


    protected $fillable = [
        'naziv',
        'temperatura',
        'vlaznost vazduha',
        'temperatura zemljista',
    ];
    
   
}
